# -*- coding: utf-8 -*-
from copy import deepcopy

from urllib.parse import urlencode

from .models import Item, Category

from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import View
from django.views.generic.list import ListView

from eap.apps.brand.models import Brand
from eap.apps.catalog.models import Color
from eap.apps.store.models import Store

from pure_pagination.mixins import PaginationMixin

from .documents import ItemSearch


class ItemView(View):
    template_name = 'catalog/item.html'

    def get(self, request, slug):
        context = {
            'item': Item.objects.get(slug=slug)
        }

        return render(request, self.template_name, context=context)


class ItemsView(PaginationMixin, ListView):
    template_name = 'catalog/items.html'

    category_field = 'category_ids'

    # Facet settings
    facet_fields = [
        {
            'name': 'brand_ids',
            'type': 'standard',
            'title': 'Brands',
            'show': True,
            'value_names': lambda: Brand.cached_names()
        },
        {
            'name': 'discounts',
            'type': 'standard',
            'title': 'Discounts',
            'show': True
        },
        {
            'name': 'in_stock',
            'type': 'standard',
            'title': 'Stock Status',
            'show': True,
            'value_names': {0: 'Out Of Stock', 1: 'In Stock'}
        },
        {
            'name': 'color_ids',
            'type': 'color',
            'title': 'Colors',
            'show': False,
            'value_names': lambda: Color.cached_names()
        },
        {
            'name': 'store_ids',
            'type': 'standard',
            'title': 'Stores',
            'show': False,
            'value_names': lambda: Store.cached_names()
        }
    ]

    # Ordering settings
    ordering = 'search_price'
    orderings = [
        # ('relevance', 'Sort by relevance'),
        # ('newest', 'Sort by newest'),
        ('search_price', 'Sort by price Ascending'),
        ('-search_price', 'Sort by price Descending')
    ]

    # Pagination settings
    paginate_by = 30

    category_slug = None
    request = None
    object_list = None

    def get(self, request, *args, **kwargs):
        self.category_slug = kwargs['slug']
        self.request = request
        self.querystring = request.GET.copy()
        context = self.get_context_data()
        return render(request, self.template_name, context=context)

    def get_context_data(self, **kwargs):
        context = kwargs
        context['object_list'] = self.get_queryset()
        context = super(ItemsView, self).get_context_data(**kwargs)

        # we need to execute query string after pagination was returned
        context['object_list'] = self.execute_queryset(context['object_list'])
        context['category'] = self.selected_category_obj
        context['total_res'] = context['object_list'].hits.total
        context['category_results'] = self._get_category_results(context['object_list'])
        context['facet_results'] = self._get_facet_results(context['object_list'])
        context['orderings'] = self._get_orderings()
        return context

    def get_queryset(self):
        queryset = ItemSearch(process_search=self._apply_filters)
        queryset = self._apply_facet_filters(queryset)
        queryset = queryset.build_search()
        queryset = self._apply_orderings(queryset)
        return queryset

    def execute_queryset(self, queryset):
        return queryset.execute()

    @property
    def selected_category_obj(self):
        return Category.objects.filter(slug=self.category_slug)[0]

    @property
    def facet_field_names(self):
        return [facet_field['name'] for facet_field in self.facet_fields]

    @property
    def current_ordering(self):
        return self.request.GET.get('ordering') or self.ordering

    def _apply_filters(self, search):
        if not self.selected_category_obj:
            return search

        search = search.filter('terms', countries=['US'.lower()])

        # Filter by selected category
        if self.selected_category_obj:
            search = search.filter('terms', categories=[self.selected_category_obj.id])

        return search

    def _apply_orderings(self, queryset):
        if not self.current_ordering:
            return queryset

        return queryset.sort(self.current_ordering)

    def _apply_facet_filters(self, queryset):
        facet_field_names = self.facet_field_names

        for field in facet_field_names:
            selected_values = self.request.GET.getlist(field)

            if selected_values:
                queryset.add_filter(field, selected_values)

        return queryset

    def _get_orderings(self):
        orderings = []
        for ordering in self.orderings:
            querystring = self.request.GET.copy()

            if 'ordering' in querystring:
                del querystring['ordering']

            # don't append ordering param to default sort
            if ordering != self.ordering:
                querystring['ordering'] = ordering[0]

            orderings.append({
                'value': ordering[0],
                'name': ordering[1],
                'active': ordering[0] == self.current_ordering,
                'querystring': urlencode(querystring, doseq=True)
            })
        return orderings

    def _get_category_results(self, object_list):
        if not self.category_field:
            return None

        category_data = {
            'name': 'Category',
            'parent_results': [],
            'results': []
        }

        parent_categories = self.selected_category_obj.get_ancestors(False, True)
        categories = self.selected_category_obj.get_children() or [self.selected_category_obj]

        for category in parent_categories:
            if len(categories) == 1 and categories[0].id == category.id:
                continue

            url = reverse('items', kwargs={'slug': category.slug})
            category_data['parent_results'].append({
                'selected': category.id == self.selected_category_obj.id,
                'name': category.name,
                'url': url
            })

        for category in categories:
            url = reverse('items', kwargs={'slug': category.slug})
            category_data['results'].append({
                'selected': category.id == self.selected_category_obj.id,
                'name': category.name,
                'url': url
            })

        return category_data

    def _get_facet_results(self, object_list):
        facet_results = []
        for field in self.facet_fields:
            results = []
            selected_facet = False
            value_names = None

            if field.get('value_names'):
                value_names = field['value_names']

                if callable(value_names):
                    # check if it's lambda or a function and if it is then call this function
                    value_names = value_names()

            for (value, count, selected) in object_list.facets[field['name']]:
                if count == 0:
                    continue  # don't include facet which doesn't have results

                # if value_names was set, then get custom value name from it
                name = value_names[int(value)] if value_names else value

                selected = str(value) in self._get_querystring().get(field['name'], [])

                if selected:
                    selected_facet = True

                facet_url = self._create_facet_url(field, value, selected)

                results.append({
                    'value': value,
                    'count': count,
                    'selected': selected,
                    'name': name,
                    'url': facet_url
                })

            field['results'] = results
            field['selected'] = selected_facet

            if results:
                facet_results.append(field)

        return facet_results

    def _create_facet_querystring(self, field, value, selected):
        querystring = deepcopy(self._get_querystring())

        if selected:
            querystring[field['name']].remove(str(value))
        else:
            if str(value) not in querystring.get(field['name'], []):

                if not querystring.get(field['name']):
                    querystring[field['name']] = []

                querystring[field['name']].append(str(value))

        return urlencode(querystring, doseq=True)

    def _create_facet_url(self, field, value, selected):
        querystring = self._create_facet_querystring(field, value, selected)
        url = reverse('items', kwargs={'slug': self.category_slug})
        return '{}?{}'.format(url, querystring) if querystring else url

    def _get_querystring(self):
        querystring = {}
        for key in self.querystring.keys():
            querystring[key] = self.querystring.getlist(key)
        return querystring

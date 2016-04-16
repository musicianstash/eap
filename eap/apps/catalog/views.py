# -*- coding: utf-8 -*-
from copy import deepcopy

from urllib.parse import urlencode

from .models import Item, Category

from django.shortcuts import render
from django.views.generic import View
from django.views.generic.list import MultipleObjectMixin

from haystack.query import SearchQuerySet

from pure_pagination import Paginator


class ItemView(View):
    template_name = 'catalog/item.html'

    def get(self, request, slug):
        context = {
            'item': Item.objects.get(slug=slug)
        }

        return render(request, self.template_name, context=context)


class ItemsView(MultipleObjectMixin, View):
    template_name = 'catalog/items.html'
    facet_fields = ['brand', 'color', 'store', 'in_stock', 'rounded_discount']
    category_slug = None
    request = None
    querystring = {}
    paginate_by = 30
    paginator_class = Paginator
    queryset = SearchQuerySet()
    object_list = None
    ordering = 'price'
    orderings = [
        ('relevance', 'Sort by relevance'),
        ('newest', 'Sort by newest'),
        ('price', 'Sort by price Ascending'),
        ('-price', 'Sort by price Descending')
    ]

    def get(self, request, *args, **kwargs):
        self.category_slug = kwargs['slug']
        self.request = request
        self.querystring = request.GET.copy()
        context = self.get_context_data(**{
            'object_list': self.get_queryset()
        })

        return render(request, self.template_name, context=context)

    def get_queryset(self):
        queryset = super(ItemsView, self).get_queryset()
        queryset = self._apply_facets(queryset)
        queryset = self._apply_facet_filters(queryset)
        # queryset = queryset.filter(countries__in=['GB'])
        queryset = queryset.filter(categories__in=[self.category_slug])
        return queryset

    def get_ordering(self):
        """ Return the field or fields to use for ordering the queryset.
        """
        return self.get_current_ordering()

    def get_context_data(self, **kwargs):
        context = kwargs
        context.update({'facets': context['object_list'].facet_counts()})
        # stats = context['object_list'].stats('discount')
        # print(stats.stats_results())
        context['facets']['fields'] = self._format_facet_fields(context['facets']['fields'])
        context['category'] = Category.objects.get(slug=self.category_slug)
        context['category_facets'] = self.get_faceted_categories(context['category'])
        context['orderings'] = self.get_orderings()
        return super(ItemsView, self).get_context_data(**kwargs)

    def get_orderings(self):
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
                'active': ordering[0] == self.get_current_ordering(),
                'querystring': urlencode(querystring, doseq=True)
            })
        return orderings

    def get_current_ordering(self):
        return self.request.GET.get('ordering') or self.ordering

    def get_faceted_categories(self, category):
        context = {
            'categories': [],
            'parent_categories': []
        }

        queryset = SearchQuerySet()
        all_categories = category.get_children()

        if all_categories:
            slug = category.slug
            parent_categories = category.get_ancestors(False, True)
        else:
            slug = category.parent.slug
            all_categories = category.get_siblings(True)
            parent_categories = category.get_ancestors(False)

        queryset = queryset.filter(categories__in=[slug])
        queryset = queryset.facet('categories')
        for field in self.facet_fields:
            selected_values = self.request.GET.getlist(field)

            if selected_values:
                queryset = queryset.filter(**{'{}__in'.format(field): selected_values})

        category_facets = queryset.facet_counts()
        format_category_facets = self._format_facet_fields(category_facets['fields'], False)
        format_category_facets = format_category_facets['categories']

        for parent_category in parent_categories:
            for format_category_facet in format_category_facets:
                if format_category_facet['value'] == parent_category.slug:
                    format_category_facet['name'] = parent_category.name
                    context['parent_categories'].append(format_category_facet)

        for category_sibling in all_categories:
            for format_category_facet in format_category_facets:
                if format_category_facet['value'] == category_sibling.slug:
                    format_category_facet['name'] = category_sibling.name
                    context['categories'].append(format_category_facet)

        return context

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True, **kwargs):
        """ Return an instance of the paginator for this view. Needs to be overidden from parent
        class because request instance needs to be passed to paginator class, bcs without that
        pagination links will have only page param in query string and others will be ignored.
        """
        return self.paginator_class(queryset, per_page, orphans=orphans,
                                    allow_empty_first_page=allow_empty_first_page,
                                    request=self.request)

    def _apply_facets(self, queryset):
        for field in self.facet_fields:
            query = '{{!ex={0}t}}{0}'.format(field)
            queryset = queryset.facet(query, missing=True)
        return queryset

    def _apply_facet_filters(self, queryset):
        for field in self.facet_fields:
            selected_values = self.request.GET.getlist(field)
            selected_values = ' OR '.join(selected_values)
            if selected_values:
                query = '{{!tag={0}t}}{0}:({1})'.format(field, selected_values)
                queryset = queryset.narrow(query)
        return queryset

    def _apply_ordering(self):
        pass

    def _format_facet_fields(self, facet_fields, include_self_in_query_string=True):
        formatted_facet_fields = {}

        for facet_key, facet_values in facet_fields.items():
            formatted_facet_values = []

            for facet_value in facet_values:
                querystring = deepcopy(self.get_querystring())

                if 'page' in querystring:
                    del querystring['page']

                active = facet_value[0] in querystring.get(facet_key, [])

                if not facet_value[1] and not active:
                    continue

                if include_self_in_query_string:
                    if active:
                        querystring[facet_key].remove(facet_value[0])
                    else:
                        if facet_value[0] not in querystring.get(facet_key, []):
                            if not querystring.get(facet_key):
                                querystring[facet_key] = []

                            querystring[facet_key].append(facet_value[0])

                value = facet_value[0]

                if value.lower() == 'true':
                    value = 'Yes'
                elif value.lower() == 'false':
                    value = 'No'

                formatted_facet_values.append({
                    'value': value,
                    'count': facet_value[1],
                    'active': active,
                    'querystring': urlencode(querystring, doseq=True)
                })

            formatted_facet_fields[facet_key] = formatted_facet_values

        return formatted_facet_fields

    def get_querystring(self):
        querystring = {}
        for key in self.querystring.keys():
            querystring[key] = self.querystring.getlist(key)
        return querystring

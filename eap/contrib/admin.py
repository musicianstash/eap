# -*- coding: utf-8 -*-
from django.contrib import admin

from mptt.admin import MPTTModelAdmin
from suit.admin import SortableModelAdmin


class SortableMPTTModelAdmin(MPTTModelAdmin, SortableModelAdmin):
    """Fix for django suit reordering so that correct order is actually shown in list.
    """
    def __init__(self, *args, **kwargs):
        super(SortableMPTTModelAdmin, self).__init__(*args, **kwargs)
        mptt_opts = self.model._mptt_meta
        # NOTE: use mptt default ordering
        self.ordering = (mptt_opts.tree_id_attr, mptt_opts.left_attr)
        if self.list_display and self.sortable not in self.list_display:
            self.list_display = list(self.list_display) + [self.sortable]

        self.list_editable = self.list_editable or []
        if self.sortable not in self.list_editable:
            self.list_editable = list(self.list_editable) + [self.sortable]

        self.exclude = self.exclude or []
        if self.sortable not in self.exclude:
            self.exclude = list(self.exclude) + [self.sortable]

    # NOTE: return default admin ChangeList
    def get_changelist(self, request, **kwargs):
        return admin.views.main.ChangeList

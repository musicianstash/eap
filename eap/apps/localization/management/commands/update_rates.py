# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError

from ...conversion import update_rates


class Command(BaseCommand):
    """This command triggers exchange update process"""

    def handle(self, *args, **options):
        """Handle command"""

        try:
            update_rates()
        except Exception as e:
            raise CommandError(e)

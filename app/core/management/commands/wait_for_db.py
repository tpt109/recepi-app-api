"""
Wait for db connection to be available
"""

import time
from psycopg2 import OperationalError as Psycopg20pError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """ Django command waiting for database connection """

    def handle(self, *args, **options):
        """Entry point for waiting for db connection"""
        self.stdout.write('Waiting for db connection...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg20pError, OperationalError):
                self.stdout.write('Database unavailable,waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))

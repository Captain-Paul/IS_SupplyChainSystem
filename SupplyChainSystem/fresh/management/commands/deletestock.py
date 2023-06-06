from fresh.models import *
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        StockInfo.objects.filter(g_id='V2023002', wh_id='BJHD0001').delete()
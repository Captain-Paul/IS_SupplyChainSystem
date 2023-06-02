from fresh.models import *
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        objects_to_create = [
            StockInfo(wh_id='BJHD0001', g_id='V2023001', s_quantity=10),
            StockInfo(wh_id='BJCY0001', g_id='F2023001', s_quantity=15),
            StockInfo(wh_id='BJCY0001', g_id='F2023002', s_quantity=10)
        ]

        StockInfo.objects.bulk_create(objects_to_create)



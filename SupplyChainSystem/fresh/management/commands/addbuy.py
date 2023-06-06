from fresh.models import *
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        objects_to_create = [
            BuyRecord(buy_id='06001', g_id='V2023001', wh_id='BJHD0001', buy_quantity=10, buy_pdate='2023-05-31'),
            BuyRecord(buy_id='06002', g_id='F2023001', wh_id='BJCY0001', buy_quantity=10, buy_pdate='2023-06-04'),
            BuyRecord(buy_id='06003', g_id='V2023002', wh_id='BJCY0001', buy_quantity=10, buy_pdate='2023-06-05'),
            BuyRecord(buy_id='06004', g_id='F2023002', wh_id='BJHD0001', buy_quantity=10, buy_pdate='2023-06-01')
        ]

        for obj in objects_to_create:
            obj.save()



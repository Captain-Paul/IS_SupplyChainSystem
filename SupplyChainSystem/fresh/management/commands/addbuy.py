from fresh.models import *
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        objects_to_create = [
            BuyRecord(g_id='V2023001', wh_id='BJHD0001', buy_quantity=10),
            BuyRecord(g_id='F2023001', wh_id='BJCY0001', buy_quantity=10)
        ]

        for obj in objects_to_create:
            obj.save()



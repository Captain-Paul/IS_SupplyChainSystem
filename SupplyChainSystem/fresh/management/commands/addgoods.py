from fresh.models import *
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        objects_to_create = [
            GoodsInfo(g_id='V2023001', g_category='Veg', g_name='芹菜', g_life=10, g_tempreture=20, g_humidity=15),
            GoodsInfo(g_id='V2023002', g_category='Veg', g_name='菠菜', g_life=10, g_tempreture=20, g_humidity=15),
            GoodsInfo(g_id='F2023001', g_category='Fruit', g_name='蓝莓', g_life=3, g_tempreture=5, g_humidity=15),
            GoodsInfo(g_id='F2023002', g_category='Fruit', g_name='香蕉', g_life=10, g_tempreture=20, g_humidity=15),
        ]

        GoodsInfo.objects.bulk_create(objects_to_create)



from fresh.models import *
from fresh.serializers import WarehouseInfoSerializer
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        objects_to_create = [
            WarehouseInfo(wh_id="BJHD0001", wh_loc="北京市海淀区学院路37号", wh_name="海淀1", wh_chief_id=5),
            WarehouseInfo(wh_id="BJCY0001", wh_loc="北京市朝阳区", wh_name="朝阳1", wh_chief_id=5)
        ]

        WarehouseInfo.objects.bulk_create(objects_to_create)



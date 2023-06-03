from fresh.models import *
from django.core.management.base import BaseCommand
from datetime import datetime


class Command(BaseCommand):
    def handle(self, *args, **options):
        objects_to_create = [
            OutboundRecord(out_id='OUT1', g_id='F2023001', wh_id='BJCY0001', out_time=datetime.now()),
            OutboundRecord(out_id='OUT2', g_id='F2023002', wh_id='BJCY0001', out_time=datetime.now())
        ]

        OutboundRecord.objects.bulk_create(objects_to_create)



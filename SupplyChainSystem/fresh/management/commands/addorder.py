from fresh.models import *
from django.core.management.base import BaseCommand
from datetime import datetime


class Command(BaseCommand):
    def handle(self, *args, **options):
        objects_to_create = [
            OrderInfo(out_id='OUT1', transfer_id='23060301', g_id='F2023001', order_time=datetime.now(), client_addr='西直门大街', order_quantity=5),
            OrderInfo(out_id='OUT2', transfer_id='23060302', g_id='F2023002', order_time=datetime.now(), client_addr='东直门大街', order_quantity=5)
        ]

        for obj in objects_to_create:
            obj.save()



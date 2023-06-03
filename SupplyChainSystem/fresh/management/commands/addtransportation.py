from fresh.models import *
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        objects_to_create = [
            TransportationInfo(transportation_id='BJV03001', transportation_class='卡车', driver_id='D001', driver_name='abc'),
            TransportationInfo(transportation_id='BJV03002', transportation_class='卡车', driver_id='D002', driver_name='def')
        ]

        TransportationInfo.objects.bulk_create(objects_to_create)



from fresh.models import *
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        objects_to_create = [
            TransferInfo(transfer_id='23060301', transfer_amount=100),
            TransferInfo(transfer_id='23060302', transfer_amount=200)
        ]

        TransferInfo.objects.bulk_create(objects_to_create)



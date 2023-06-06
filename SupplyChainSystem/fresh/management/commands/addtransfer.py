from fresh.models import *
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        objects_to_create = [
            TransferInfo(transfer_id='23060301', transfer_amount=100, transfer_inaccount='fresh_bank_account',
                         transfer_outaccount='xyf_bank_account', transfer_class='in', transfer_staffid=3),
            TransferInfo(transfer_id='23060302', transfer_amount=200, transfer_inaccount='xyy_bank_account',
                         transfer_outaccount='fresh_bank_account', transfer_class='out', transfer_staffid=3)
        ]

        TransferInfo.objects.bulk_create(objects_to_create)



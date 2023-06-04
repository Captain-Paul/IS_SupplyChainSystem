from Login.models import *
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, User
from django.db.utils import IntegrityError
from faker import Faker  # 随机人名


class Command(BaseCommand):
    def handle(self, *args, **options):
        groups = ['hr', 'trans', 'fin', 'sale', 'store']
        for group_dp in groups:
            # create or get department groups
            group, created = Group.objects.get_or_create(name=group_dp)

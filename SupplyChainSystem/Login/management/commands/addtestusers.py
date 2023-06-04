from Login.models import *
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, User
from django.db.utils import IntegrityError
from faker import Faker # 随机人名


class Command(BaseCommand):
    def handle(self, *args, **options):
        # objects_to_create = [
        #     BuyRecord(g_id='V2023001', wh_id='BJHD0001', buy_quantity=10),
        #     BuyRecord(g_id='F2023001', wh_id='BJCY0001', buy_quantity=10)
        # ]
        #
        # for obj in objects_to_create:
        #     obj.save()
        groups = ['hr', 'trans', 'fin', 'sale', 'store']
        count = 1
        for group_dp in groups:
            try:
                # create or get department groups
                group, created = Group.objects.get_or_create(name=group_dp)
                # create or get staffs & users for test
                username = f"staff{count:04}"
                try:
                    # 尝试获取已经存在的用户信息
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    # 若不存在，则创建新的用户对象
                    user = User.objects.create_user(username=username, password='123456')
                    print(username + " has been registered.")
                # user = User.objects.create_user(username=group_dp+' staff', password='123456')
                user.groups.add(group)
                # 将用户信息同步到 StaffInfo 表中
                staff_info = StaffInfo(user=user, s_id=str(count), s_name='_'+Faker('zh_CN').name(),
                                       s_salary=10000, s_onboard_date='2023-06-01 08:00:00',
                                       s_gender='男', s_birth='1990-01-01 00:00:00', s_job='员工',
                                       s_email='test@test.com', s_tel='12345678901')
                staff_info.save()
                StaffInfo.count += 1
                count += 1
            except IntegrityError:
                # 用户名重复，不再创建
                print('test user already exists in ' + group_dp)
                pass

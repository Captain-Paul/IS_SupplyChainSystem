from Login.models import *
from django.core.management.base import BaseCommand
import random   # 随机kpi
from django.contrib.auth.models import User
from datetime import datetime
import random


class Command(BaseCommand):
    def handle(self, *args, **options):
        objects_to_create = []
        for i in range(1, 6):
            # 获取测试的用户
            username = f"staff{i:04}"
            user = User.objects.get(username=username)
            # 生成随机年月时间
            year = random.randint(2022, 2023)
            month = random.randint(1, 12)
            k_ym = datetime(year, month, 1)
            # 生成随机绩效
            kpi = round(random.uniform(0, 100), 3)
            # 计算实际工资
            real_salary = StaffInfo.objects.get(user=user).s_salary + (kpi - 50) * 10
            # 创建 KpiInfo 对象并添加到列表中
            object_to_create = KpiInfo(k_id=str(i), user=user, k_ym=k_ym, kpi=kpi, real_salary=real_salary)
            object_to_create.save()
            print(f"a new kpi record has been added: k_id={str(i)}, user={user}, k_ym={k_ym} kpi={kpi}, real_salary={real_salary}")

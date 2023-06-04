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
            k_user = User.objects.get(username=username)
            # 生成随机年月时间
            year = random.randint(2022, 2023)
            month = random.randint(1, 12)
            k_ym = datetime(year, month, 1)
            # 生成随机绩效
            kpi = round(random.uniform(0, 100), 3)
            # 计算实际工资
            realsalary = StaffInfo.objects.get(s_user=k_user).s_salary + (kpi - 50) * 10
            # 创建 KpiInfo 对象并添加到列表中
            objects_to_create.append(KpiInfo(k_id=str(i), k_user=k_user, k_ym=k_ym, kpi=kpi, realsalary=realsalary))
        KpiInfo.objects.bulk_create(objects_to_create)

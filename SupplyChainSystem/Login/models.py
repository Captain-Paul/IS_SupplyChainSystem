from django.db import models
from django.conf import settings

class StaffInfo(models.Model):
    s_id = models.CharField(primary_key=True, max_length=8, verbose_name="员工编号")
    s_name = models.CharField(max_length=16, verbose_name="员工姓名", blank=True, null=True)
    s_salary = models.BigIntegerField(verbose_name="基本工资", blank=True, null=True)
    s_onboarddate = models.DateTimeField(verbose_name="上岗日期", blank=True, null=True)
    s_gender = models.CharField(max_length=4, verbose_name="性别", blank=True, null=True)
    s_birth = models.DateTimeField(verbose_name="生日", blank=True, null=True)
    s_department = models.CharField(max_length=16, verbose_name="所属部门", blank=True, null=True)
    s_job = models.TextField(verbose_name="职务", blank=True, null=True)  # This field type is a guess.
    s_email = models.CharField(max_length=64, verbose_name="邮箱", blank=True, null=True)
    s_tel = models.CharField(max_length=64, verbose_name="联系电话", blank=True, null=True)
    s_pw = models.CharField(max_length=64, verbose_name="密码", blank=True, null=True)
    count = 0

    def save(self):
        if not self.s_id:
            count += 1
            self.s_id = s_department[:2] + str(count)
        super().save()

    class Meta:
        verbose_name = '员工信息'
        verbose_name_plural = verbose_name
        db_table = 'staff_info'


class KpiInfo(models.Model):
    k_id = models.AutoField(primary_key=True, verbose_name="KPI编号")
    k_ym = models.DateTimeField(verbose_name="年月", blank=False, null=False)
    s = models.ForeignKey('StaffInfo', verbose_name="员工编号", on_delete=models.CASCADE)
    kpi = models.FloatField(verbose_name="绩效", blank=True, null=True)
    realsalary = models.BigIntegerField(verbose_name="实发工资", blank=True, null=True)

    class Meta:
        verbose_name = '员工绩效信息'
        verbose_name_plural = verbose_name
        db_table = 'KPI_info'

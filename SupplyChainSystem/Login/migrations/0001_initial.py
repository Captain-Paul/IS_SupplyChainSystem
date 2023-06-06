# Generated by Django 4.1.7 on 2023-06-06 22:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="StaffInfo",
            fields=[
                (
                    "s_id",
                    models.CharField(
                        max_length=8,
                        primary_key=True,
                        serialize=False,
                        verbose_name="员工编号",
                    ),
                ),
                (
                    "s_name",
                    models.CharField(
                        blank=True, max_length=16, null=True, verbose_name="员工姓名"
                    ),
                ),
                (
                    "s_salary",
                    models.BigIntegerField(blank=True, null=True, verbose_name="基本工资"),
                ),
                (
                    "s_onboard_date",
                    models.DateTimeField(blank=True, null=True, verbose_name="上岗日期"),
                ),
                (
                    "s_gender",
                    models.CharField(
                        blank=True, max_length=4, null=True, verbose_name="性别"
                    ),
                ),
                (
                    "s_birth",
                    models.DateTimeField(blank=True, null=True, verbose_name="生日"),
                ),
                ("s_job", models.TextField(blank=True, null=True, verbose_name="职务")),
                (
                    "s_email",
                    models.CharField(
                        blank=True, max_length=64, null=True, verbose_name="邮箱"
                    ),
                ),
                (
                    "s_tel",
                    models.CharField(
                        blank=True, max_length=64, null=True, verbose_name="联系电话"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="用户编号",
                    ),
                ),
            ],
            options={
                "verbose_name": "员工信息",
                "verbose_name_plural": "员工信息",
                "db_table": "staff_info",
            },
        ),
        migrations.CreateModel(
            name="KpiInfo",
            fields=[
                (
                    "k_id",
                    models.CharField(
                        max_length=8,
                        primary_key=True,
                        serialize=False,
                        verbose_name="KPI编号",
                    ),
                ),
                ("k_ym", models.DateTimeField(verbose_name="年月")),
                ("kpi", models.FloatField(blank=True, null=True, verbose_name="绩效")),
                (
                    "real_salary",
                    models.BigIntegerField(blank=True, null=True, verbose_name="实发工资"),
                ),
                (
                    "s_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Login.staffinfo",
                        verbose_name="员工编号",
                    ),
                ),
            ],
            options={
                "verbose_name": "员工绩效信息",
                "verbose_name_plural": "员工绩效信息",
                "db_table": "KPI_info",
            },
        ),
    ]

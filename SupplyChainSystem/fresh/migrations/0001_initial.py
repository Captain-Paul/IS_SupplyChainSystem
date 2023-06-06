# Generated by Django 4.1.7 on 2023-06-06 21:54

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
            name="GoodsInfo",
            fields=[
                (
                    "g_id",
                    models.CharField(
                        max_length=8,
                        primary_key=True,
                        serialize=False,
                        verbose_name="货物编号",
                    ),
                ),
                (
                    "g_brand",
                    models.CharField(
                        blank=True, max_length=16, null=True, verbose_name="货物品牌"
                    ),
                ),
                (
                    "g_category",
                    models.CharField(
                        blank=True, max_length=16, null=True, verbose_name="货物种类"
                    ),
                ),
                (
                    "g_name",
                    models.CharField(
                        blank=True, max_length=16, null=True, verbose_name="货物名称"
                    ),
                ),
                (
                    "g_life",
                    models.IntegerField(blank=True, null=True, verbose_name="保质期"),
                ),
                ("g_loc", models.TextField(blank=True, null=True, verbose_name="地址")),
                (
                    "g_vendor",
                    models.CharField(
                        blank=True, max_length=16, null=True, verbose_name="供应商"
                    ),
                ),
                (
                    "g_tempreture",
                    models.FloatField(default=5, null=True, verbose_name="储存温度"),
                ),
                (
                    "g_humidity",
                    models.FloatField(default=85, null=True, verbose_name="储存湿度"),
                ),
            ],
            options={
                "verbose_name": "货物信息",
                "verbose_name_plural": "货物信息",
                "db_table": "goods_info",
            },
        ),
        migrations.CreateModel(
            name="OrderInfo",
            fields=[
                (
                    "order_id",
                    models.CharField(
                        max_length=20,
                        primary_key=True,
                        serialize=False,
                        verbose_name="订单编号",
                    ),
                ),
                ("order_time", models.DateTimeField(null=True, verbose_name="生效时间")),
                (
                    "order_quantity",
                    models.SmallIntegerField(
                        blank=True, null=True, verbose_name="订单数量"
                    ),
                ),
                (
                    "order_realprice",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=6,
                        null=True,
                        verbose_name="实际售价",
                    ),
                ),
                (
                    "client_name",
                    models.CharField(
                        blank=True, max_length=16, null=True, verbose_name="客户姓名"
                    ),
                ),
                (
                    "client_addr",
                    models.CharField(
                        blank=True, max_length=16, null=True, verbose_name="客户地址"
                    ),
                ),
                (
                    "client_tel",
                    models.CharField(
                        blank=True, max_length=11, null=True, verbose_name="客户电话"
                    ),
                ),
                (
                    "g",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fresh.goodsinfo",
                        verbose_name="货物编码",
                    ),
                ),
            ],
            options={
                "verbose_name": "订单信息",
                "verbose_name_plural": "订单信息",
                "db_table": "order_info",
            },
        ),
        migrations.CreateModel(
            name="TransportationInfo",
            fields=[
                (
                    "transportation_id",
                    models.CharField(
                        max_length=8,
                        primary_key=True,
                        serialize=False,
                        verbose_name="载具编号",
                    ),
                ),
                (
                    "transportation_class",
                    models.TextField(blank=True, null=True, verbose_name="载具类型"),
                ),
                (
                    "driver_name",
                    models.CharField(
                        blank=True, max_length=16, null=True, verbose_name="驾驶人姓名"
                    ),
                ),
                (
                    "driver_id",
                    models.CharField(
                        blank=True, max_length=8, null=True, verbose_name="驾驶人编号"
                    ),
                ),
            ],
            options={
                "verbose_name": "载具信息",
                "verbose_name_plural": "载具信息",
                "db_table": "transportation_info",
            },
        ),
        migrations.CreateModel(
            name="WarehouseInfo",
            fields=[
                (
                    "wh_id",
                    models.CharField(
                        max_length=8,
                        primary_key=True,
                        serialize=False,
                        verbose_name="仓库编号",
                    ),
                ),
                (
                    "wh_loc",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="仓库位置"
                    ),
                ),
                (
                    "wh_name",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="仓库名称"
                    ),
                ),
                (
                    "wh_chief",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="责任人",
                    ),
                ),
            ],
            options={
                "verbose_name": "仓库信息",
                "verbose_name_plural": "仓库信息",
                "db_table": "warehouse_info",
            },
        ),
        migrations.CreateModel(
            name="TransportRecord",
            fields=[
                (
                    "transport_id",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="运输编码"
                    ),
                ),
                (
                    "transport_to",
                    models.CharField(
                        blank=True, max_length=16, null=True, verbose_name="目的地"
                    ),
                ),
                (
                    "transport_predicatedtime",
                    models.DateTimeField(blank=True, null=True, verbose_name="预计送达时间"),
                ),
                (
                    "transport_realtime",
                    models.DateTimeField(blank=True, null=True, verbose_name="实际送达时间"),
                ),
                (
                    "order",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fresh.orderinfo",
                        verbose_name="订单编号",
                    ),
                ),
                (
                    "transportation",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fresh.transportationinfo",
                        verbose_name="载具编号",
                    ),
                ),
                (
                    "wh",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fresh.warehouseinfo",
                        verbose_name="仓库编码",
                    ),
                ),
            ],
            options={
                "verbose_name": "运输记录",
                "verbose_name_plural": "运输记录",
                "db_table": "transport_record",
            },
        ),
        migrations.CreateModel(
            name="TransferInfo",
            fields=[
                (
                    "transfer_id",
                    models.CharField(
                        max_length=8,
                        primary_key=True,
                        serialize=False,
                        verbose_name="交易编码",
                    ),
                ),
                (
                    "transfer_amount",
                    models.BigIntegerField(blank=True, null=True, verbose_name="金额"),
                ),
                (
                    "transfer_inaccount",
                    models.CharField(
                        blank=True, max_length=19, null=True, verbose_name="收款账户"
                    ),
                ),
                (
                    "transfer_outaccount",
                    models.CharField(
                        blank=True, max_length=19, null=True, verbose_name="付款账户"
                    ),
                ),
                (
                    "transfer_class",
                    models.CharField(
                        blank=True, max_length=4, null=True, verbose_name="转账类型"
                    ),
                ),
                (
                    "transfer_staffid",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="业务员编号",
                    ),
                ),
            ],
            options={
                "verbose_name": "转账信息",
                "verbose_name_plural": "转账信息",
                "db_table": "transfer_info",
            },
        ),
        migrations.CreateModel(
            name="StockInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "s_quantity",
                    models.SmallIntegerField(
                        blank=True, null=True, verbose_name="库存数量"
                    ),
                ),
                (
                    "g",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fresh.goodsinfo",
                        verbose_name="货物编码",
                    ),
                ),
                (
                    "wh",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fresh.warehouseinfo",
                        verbose_name="仓库编码",
                    ),
                ),
            ],
            options={
                "verbose_name": "库存信息",
                "verbose_name_plural": "库存信息",
                "db_table": "stock_info",
            },
        ),
        migrations.CreateModel(
            name="OutboundRecord",
            fields=[
                (
                    "out_id",
                    models.CharField(
                        max_length=8,
                        primary_key=True,
                        serialize=False,
                        verbose_name="出库编号",
                    ),
                ),
                (
                    "out_time",
                    models.DateTimeField(blank=True, null=True, verbose_name="出库时间"),
                ),
                (
                    "g",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fresh.goodsinfo",
                        verbose_name="货物编码",
                    ),
                ),
                (
                    "wh",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fresh.warehouseinfo",
                        verbose_name="仓库编码",
                    ),
                ),
            ],
            options={
                "verbose_name": "出库记录",
                "verbose_name_plural": "出库记录",
                "db_table": "outbound_record",
            },
        ),
        migrations.AddField(
            model_name="orderinfo",
            name="out",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="fresh.outboundrecord",
                verbose_name="出库编号",
            ),
        ),
        migrations.AddField(
            model_name="orderinfo",
            name="transfer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="fresh.transferinfo",
                verbose_name="交易编码",
            ),
        ),
        migrations.CreateModel(
            name="CountRecord",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "count_date",
                    models.DateField(auto_now_add=True, null=True, verbose_name="盘点日期"),
                ),
                (
                    "count_match",
                    models.CharField(
                        blank=True, max_length=4, null=True, verbose_name="是否匹配"
                    ),
                ),
                (
                    "count_quantity",
                    models.SmallIntegerField(
                        blank=True, null=True, verbose_name="现有库存"
                    ),
                ),
                (
                    "g",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fresh.goodsinfo",
                        verbose_name="货物编码",
                    ),
                ),
                (
                    "wh",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fresh.warehouseinfo",
                        verbose_name="仓库编码",
                    ),
                ),
            ],
            options={
                "verbose_name": "盘点记录",
                "verbose_name_plural": "盘点记录",
                "db_table": "count_record",
            },
        ),
        migrations.CreateModel(
            name="BuyRecord",
            fields=[
                (
                    "buy_id",
                    models.CharField(
                        blank=True,
                        max_length=8,
                        primary_key=True,
                        serialize=False,
                        verbose_name="批次编码",
                    ),
                ),
                (
                    "buy_quantity",
                    models.SmallIntegerField(
                        blank=True, null=True, verbose_name="采购数量"
                    ),
                ),
                (
                    "buy_intime",
                    models.DateField(blank=True, null=True, verbose_name="到达日期"),
                ),
                (
                    "buy_pdate",
                    models.DateField(blank=True, null=True, verbose_name="生产日期"),
                ),
                (
                    "buy_price",
                    models.BigIntegerField(blank=True, null=True, verbose_name="采购价格"),
                ),
                (
                    "buy_valid",
                    models.CharField(
                        blank=True, max_length=4, null=True, verbose_name="是否生效"
                    ),
                ),
                (
                    "return_reason",
                    models.TextField(
                        blank=True,
                        db_collation="Chinese_PRC_CI_AS",
                        null=True,
                        verbose_name="退货原因",
                    ),
                ),
                (
                    "g",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fresh.goodsinfo",
                        verbose_name="货物编码",
                    ),
                ),
                (
                    "wh",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fresh.warehouseinfo",
                        verbose_name="仓库编码",
                    ),
                ),
            ],
            options={
                "verbose_name": "采购记录",
                "verbose_name_plural": "采购记录",
                "db_table": "buy_record",
            },
        ),
        migrations.AddConstraint(
            model_name="stockinfo",
            constraint=models.UniqueConstraint(
                fields=("g", "wh"), name="unique_primary_keys_stock"
            ),
        ),
    ]

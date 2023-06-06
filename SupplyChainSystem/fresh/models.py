# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with unique=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.conf import settings
from datetime import date, datetime


"""要调用save方法的：BuyRecord, OrderInfo"""

# class StaffInfo(models.Model):
#     s_id = models.CharField(primary_key=True, max_length=8, verbose_name="员工编号")
#     s_name = models.CharField(max_length=16, verbose_name="员工姓名", blank=True, null=True)
#     s_salary = models.BigIntegerField(verbose_name="基本工资", blank=True, null=True)
#     s_onboarddate = models.DateTimeField(verbose_name="上岗日期", blank=True, null=True)
#     s_gender = models.CharField(max_length=4, verbose_name="性别", blank=True, null=True)
#     s_birth = models.DateTimeField(verbose_name="生日", blank=True, null=True)
#     s_department = models.CharField(max_length=16, verbose_name="所属部门", blank=True, null=True)
#     s_job = models.TextField(verbose_name="职务", blank=True, null=True)  # This field type is a guess.
#     s_email = models.CharField(max_length=64, verbose_name="邮箱", blank=True, null=True)
#     s_tel = models.CharField(max_length=64, verbose_name="联系电话", blank=True, null=True)
#     count = 0
#
#     def save(self):
#         if not self.s_id:
#             count += 1
#             self.s_id = s_department[:2] + str(count)
#         super().save()
#
#     class Meta:
#         verbose_name = '员工信息'
#         verbose_name_plural = verbose_name
#         db_table = 'staff_info'


# class KpiInfo(models.Model):
#     k_ym = models.DateTimeField(verbose_name="年月", primary_key=True)
#     s = models.ForeignKey('StaffInfo', verbose_name="员工编号", on_delete=models.CASCADE)
#     kpi = models.FloatField(verbose_name="绩效", blank=True, null=True)
#     realsalary = models.BigIntegerField(verbose_name="实发工资", blank=True, null=True)
#
#     class Meta:
#         verbose_name = '员工绩效信息'
#         verbose_name_plural = verbose_name
#         db_table = 'KPI_info'


class GoodsInfo(models.Model):
    g_id = models.CharField(primary_key=True, max_length=8, verbose_name="货物编号")
    g_brand = models.CharField(max_length=16, verbose_name="货物品牌", blank=True, null=True)
    g_category = models.CharField(max_length=16, verbose_name="货物种类", blank=True, null=True)
    g_name = models.CharField(max_length=16, verbose_name="货物名称", blank=True, null=True)
    g_life = models.IntegerField(verbose_name="保质期", blank=True, null=True)
    g_loc = models.TextField(verbose_name="地址", blank=True, null=True)  # This field type is a guess.
    g_vendor = models.CharField(verbose_name="供应商", max_length=16, blank=True, null=True)
    g_tempreture = models.FloatField(verbose_name="储存温度", null=True, default=5)
    g_humidity = models.FloatField(verbose_name="储存湿度", null=True, default=85)

    class Meta:
        verbose_name = '货物信息'
        verbose_name_plural = verbose_name
        db_table = 'goods_info'


class WarehouseInfo(models.Model):
    wh_id = models.CharField(primary_key=True, max_length=8, verbose_name="仓库编号")
    wh_loc = models.CharField(max_length=100, verbose_name="仓库位置", blank=True, null=True)
    wh_name = models.CharField(max_length=100, verbose_name="仓库名称", blank=True, null=True)
    # wh_chief = models.CharField(max_length=16, verbose_name="责任人", blank=True, null=True)
    wh_chief = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="责任人", null=True)

    class Meta:
        verbose_name = '仓库信息'
        verbose_name_plural = verbose_name
        db_table = 'warehouse_info'


class BuyRecord(models.Model):
    g = models.ForeignKey('GoodsInfo', verbose_name="货物编码", on_delete=models.CASCADE)
    wh = models.ForeignKey('WarehouseInfo', verbose_name="仓库编码", on_delete=models.CASCADE)
    buy_id = models.CharField(primary_key=True, max_length=8, verbose_name="批次编码", blank=True)
    buy_quantity = models.SmallIntegerField(verbose_name="采购数量", blank=True, null=True)
    buy_intime = models.DateField(verbose_name="到达日期", blank=True, null=True)
    buy_pdate = models.DateField(verbose_name="生产日期", blank=True, null=True)
    buy_price = models.BigIntegerField(verbose_name="采购价格", blank=True, null=True)
    buy_valid = models.CharField(max_length=4, verbose_name="是否生效", blank=True, null=True)
    return_reason = models.TextField(verbose_name="退货原因", db_collation='Chinese_PRC_CI_AS', blank=True, null=True)  # This field type is a guess.

    def save(self, *args, **kwargs):
        super(BuyRecord, self).save(*args, **kwargs)

        goods, created = StockInfo.objects.get_or_create(g_id=self.g_id, wh_id=self.wh_id, defaults={'s_quantity':0})
        goods.s_quantity += self.buy_quantity
        goods.save()

    class Meta:
        verbose_name = '采购记录'
        verbose_name_plural = verbose_name
        db_table = 'buy_record'
        # constraints = [
        #     models.UniqueConstraint(fields=['g', 'buy_id'], name='unique_primary_keys_buy')
        # ]


class CountRecord(models.Model):
    g = models.ForeignKey('GoodsInfo', verbose_name="货物编码", on_delete=models.CASCADE)
    wh = models.ForeignKey('WarehouseInfo', verbose_name="仓库编码", on_delete=models.CASCADE)
    count_date = models.DateField(auto_now_add=True, verbose_name="盘点日期", null=True)
    count_match = models.CharField(max_length=4, verbose_name="是否匹配", blank=True, null=True)
    count_quantity = models.SmallIntegerField(verbose_name="现有库存", blank=True, null=True)

    class Meta:
        verbose_name = '盘点记录'
        verbose_name_plural = verbose_name
        db_table = 'count_record'

count = 0
pre = date.today()
class OrderInfo(models.Model):
    order_id = models.CharField(primary_key=True, max_length=20, verbose_name="订单编号")
    transfer = models.ForeignKey('TransferInfo', verbose_name="交易编码", on_delete=models.CASCADE, null=True)
    out = models.ForeignKey('OutboundRecord', verbose_name="出库编号", on_delete=models.CASCADE, null=True)
    # transport = models.ForeignKey('TransportRecord', verbose_name="运输编码", on_delete=models.CASCADE)
    g = models.ForeignKey('GoodsInfo', verbose_name="货物编码", on_delete=models.CASCADE, null=True)
    order_time = models.DateTimeField(verbose_name="生效时间", null=True)
    order_quantity = models.SmallIntegerField(verbose_name="订单数量", blank=True, null=True)
    order_realprice = models.DecimalField(verbose_name="实际售价", max_digits=6, decimal_places=2, blank=True, null=True)
    client_name = models.CharField(max_length=16, verbose_name="客户姓名", blank=True, null=True)
    client_addr = models.CharField(max_length=16, verbose_name="客户地址", blank=True, null=True)
    client_tel = models.CharField(max_length=11, verbose_name="客户电话", blank=True, null=True)
    count = 0

    def save(self, *args, **kwargs):
        if not self.order_time:
            self.order_time = datetime.now()

        global count, pre
        count = len(OrderInfo.objects.filter(order_time__day=int(str(date.today())[-1])))
        today = date.today()
        if today != pre:
            count = 0
        count += 1
        if not self.order_id or len(self.order_id) < 10:
            self.order_id = str(date.today()) + str(count)  #将id设置为日期+序号
        pre = today
        super(OrderInfo, self).save(*args, **kwargs)

        ob, _ = OutboundRecord.objects.get_or_create(out_id=self.out_id)
        goods, _ = StockInfo.objects.get_or_create(g_id=self.g_id, wh_id=ob.wh_id)
        goods.s_quantity -= self.order_quantity
        goods.save()

        trans = TransportRecord()
        trans.transport_to = self.client_addr
        trans.wh = ob.wh
        trans.order = self
        trans.save()

    class Meta:
        verbose_name = '订单信息'
        verbose_name_plural = verbose_name
        db_table = 'order_info'


class OutboundRecord(models.Model):
    out_id = models.CharField(primary_key=True, max_length=8, verbose_name="出库编号")
    wh = models.ForeignKey('WarehouseInfo', verbose_name="仓库编码", on_delete=models.CASCADE)
    g = models.ForeignKey('GoodsInfo', verbose_name="货物编码", on_delete=models.CASCADE)
    out_time = models.DateTimeField(verbose_name="出库时间", blank=True, null=True)

    class Meta:
        verbose_name = '出库记录'
        verbose_name_plural = verbose_name
        db_table = 'outbound_record'


class StockInfo(models.Model):
    wh = models.ForeignKey('WarehouseInfo', verbose_name="仓库编码", on_delete=models.CASCADE)
    g = models.ForeignKey('GoodsInfo', verbose_name="货物编码", on_delete=models.CASCADE)
    s_quantity = models.SmallIntegerField(verbose_name="库存数量", blank=True, null=True)

    class Meta:
        verbose_name = '库存信息'
        verbose_name_plural = verbose_name
        db_table = 'stock_info'
        constraints = [
            models.UniqueConstraint(fields=['g', 'wh'], name='unique_primary_keys_stock')
        ]


class TransportationInfo(models.Model):
    transportation_id = models.CharField(primary_key=True, max_length=8, verbose_name="载具编号")
    transportation_class = models.TextField(verbose_name="载具类型", blank=True, null=True)  # This field type is a guess.
    driver_name = models.CharField(max_length=16, verbose_name="驾驶人姓名", blank=True, null=True)
    driver_id = models.CharField(max_length=8, verbose_name="驾驶人编号", blank=True, null=True)

    class Meta:
        verbose_name = '载具信息'
        verbose_name_plural = verbose_name
        db_table = 'transportation_info'


class TransportRecord(models.Model):
    transport_id = models.AutoField(primary_key=True, verbose_name="运输编码")
    order = models.ForeignKey('OrderInfo', verbose_name='订单编号', on_delete=models.CASCADE, null=True)
    transportation = models.ForeignKey('TransportationInfo', verbose_name="载具编号", on_delete=models.CASCADE, null=True)
    wh = models.ForeignKey('WarehouseInfo', verbose_name="仓库编码", on_delete=models.CASCADE)
    transport_to = models.CharField(max_length=16, verbose_name="目的地", blank=True, null=True)
    transport_predicatedtime = models.DateTimeField(verbose_name="预计送达时间", blank=True, null=True)
    transport_realtime = models.DateTimeField(verbose_name="实际送达时间", blank=True, null=True)

    class Meta:
        verbose_name = '运输记录'
        verbose_name_plural = verbose_name
        db_table = 'transport_record'


class TransferInfo(models.Model):
    transfer_id = models.CharField(primary_key=True, max_length=8, verbose_name="交易编码")
    transfer_amount = models.BigIntegerField(verbose_name="金额", blank=True, null=True)
    transfer_inaccount = models.CharField(max_length=19, verbose_name="收款账户", blank=True, null=True)
    transfer_outaccount = models.CharField(max_length=19, verbose_name="付款账户", blank=True, null=True)
    transfer_class = models.CharField(max_length=4, verbose_name="转账类型", blank=True, null=True)
    # transfer_staffid = models.CharField(max_length=8, db_collation='Chinese_PRC_CI_AS', blank=True, null=True)
    transfer_staffid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="业务员编号", null=True)
    # transfer_staffname = models.CharField(max_length=16, db_collation='Chinese_PRC_CI_AS', blank=True, null=True)

    class Meta:
        verbose_name = '转账信息'
        verbose_name_plural = verbose_name
        db_table = 'transfer_info'
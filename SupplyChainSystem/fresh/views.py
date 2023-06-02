from django.shortcuts import render

from django.db.models.signals import post_save
from django.db.models import Q, F, ExpressionWrapper, Func
from django.db.models.fields import DurationField
from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerReadOnly

from .models import *
from .serializers import *
import json
from datetime import date, timedelta
# 导入员工信息和KPI
from Login.models import *
from Login.serializers import *

# # 内存缓存
# from django.core.cache import cache
# import pyodbc

class FreshPagination(PageNumberPagination):
    '''
    分页属性
    '''
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

# # 用户登录状态缓存
# def user_login(request):
#     """
#     在登录视图中，在用户成功登录后将登录信息写入缓存。
#     :param request:
#     :return:
#     """
#     if user and user.is_active:
#         # 登录成功，将登录信息写入缓存
#         conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=your_db_host;DATABASE=your_db_name;UID=your_db_username;PWD=your_db_password')
#         cursor = conn.cursor()
#         cursor.execute(f"SELECT COUNT(*) FROM dbo.[auth_user] WHERE id = '{user.id}'")
#         result = cursor.fetchone()
#         if result[0] == 1:  # 用户存在
#             cache.set(f'user:{user.id}:login', True, timeout=None)  # 缓存永不过期，即在浏览器关闭前一直有效
#         cursor.close()
#         conn.close()
#
# class Logintest(APIView):
#     def dispatch(self, request, *args, **kwargs):
#         # 检查用户是否已登录，如果未登录则返回错误响应
#         user_id = request.user.id  # 获取当前请求的用户ID
#         conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=your_db_host;DATABASE=your_db_name;UID=your_db_username;PWD=your_db_password')
#         cursor = conn.cursor()
#         cursor.execute(f"SELECT COUNT(*) FROM dbo.[auth_user] WHERE id = '{user_id}'")
#         result = cursor.fetchone()
#         if result[0] == 1:  # 用户存在
#             is_logged_in = cache.get(f'user:{user_id}:login', False)  # 从缓存中获取登录信息
#             if is_logged_in:
#                 # 用户已经登录，继续处理请求
#                 cursor.close()
#                 conn.close()
#                 return super().dispatch(request, *args, **kwargs)
#
#         # 用户未登录或登录信息不正确，返回错误响应
#         cursor.close()
#         conn.close()
#         return HttpResponse('Unauthorized', status=401)



class GoodsList(APIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = FreshPagination

    def get(self, request):
        """
        返回所有数据
        :param request:
        :return:
        """
        queryset = GoodsInfo.objects.all()
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            s = GoodsInfoSerializer(instance=page, many=True)
            return paginator.get_paginated_response(s.data)

        s = GoodsInfoSerializer(instance=queryset, many=True)
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        新增一条数据
        :param request:
        :return:
        """
        s = GoodsInfoSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


class GoodsDetail(APIView):
    @staticmethod
    def get_object(pk):
        """
        Get object according to given primary key.
        :param pk:
        :return:
        """
        try:
            return GoodsInfo.objects.get(pk=pk)
        except:
            return

    def get(self, request):
        """
        :param request:
        :return:
        """
        g_id = request.GET.get('g_id')
        if g_id:
            obj = self.get_object(pk=g_id)
            if not obj:
                return Response(data={"msg": "没有此货物信息"}, status=status.HTTP_404_NOT_FOUND)
            s = GoodsInfoSerializer(instance=obj)
            return Response(s.data, status=status.HTTP_200_OK)

    def put(self, request):
        """
        修改一条数据
        :param request:
        :return:
        """
        body = request.body
        try:
            data = json.loads(body.decode('utf-8'))
        except ValueError:
            return Response(data={"msg": "非合法json格式"}, status=status.HTTP_404_NOT_FOUND)

        g_id = data.get('g_id')
        obj = self.get_object(pk=g_id)
        if not obj:
            return Response(data={"msg": "没有此货物信息"}, status=status.HTTP_404_NOT_FOUND)
        s = GoodsInfoSerializer(instance=obj, data=request.data)
        if s.is_valid():
            s.save()
            return Response(data=s.data, status=status.HTTP_200_OK)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


class WarehouseList(APIView):
    def get(self, request):
        """
        返回所有仓库信息
        :param request:
        :return:
        """
        queryset = WarehouseInfo.objects.all()
        s = WarehouseInfoSerializer(instance=queryset, many=True)
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        添加一条仓库信息
        :param request:
        :return:
        """
        s = WarehouseInfoSerializer(data=request.data)
        if s.is_valid():
            s.save(wh_chief=self.request.user)
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


class WarehouseDetail(APIView):
    @staticmethod
    def get_object(pk):
        try:
            return WarehouseInfo.objects.get(pk=pk)
        except:
            return

    def get(self, request):
        func = request.GET.get('function')
        #按照id查询仓库
        if func == "id":
            wh_id = request.GET.get('wh_id')
            obj = self.get_object(pk=wh_id)
            if not obj:
                return Response(data={"msg": "没有此仓库信息"}, status=status.HTTP_404_NOT_FOUND)
            s = WarehouseInfoSerializer(instance=obj)
            return Response(s.data, status=status.HTTP_200_OK)

        #查询距离接收到的坐标最近的仓库
        if func == 'nearest':
            loc = request.query_params.get('loc', None)  # 获取请求中的经纬度参数
            if loc:
                try:
                    lat, lng = loc.split(',')  # 将经纬度字符串解析为两个数值
                    lat, lng = float(lat), float(lng)
                except ValueError:
                    return Response({'error': 'Invalid location parameter'}, status=status.HTTP_400_BAD_REQUEST)
                # 查询最近的仓库，使用Django提供的geo查询API
                warehouse = WarehouseInfo.objects.annotate(distance=Distance('location', Point(lng, lat))).order_by('distance').first()
                if warehouse:
                    serializer = WarehouseSerializer(warehouse)
                    return Response(serializer.data)
                else:
                    return Response({'error': 'No warehouse found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        body = request.body
        try:
            data = json.loads(body.decode('utf-8'))
        except ValueError:
            return Response(data={"msg": "非合法json格式"}, status=status.HTTP_404_NOT_FOUND)

        wh_id = data.get('wh_id')
        obj = self.get_object(pk=wh_id)
        if not obj:
            return Response(data={"msg": "没有此仓库信息"}, status=status.HTTP_404_NOT_FOUND)
        s = WarehouseInfoSerializer(instance=obj, data=request.data)
        if s.is_valid():
            s.save()
            return Response(data=s.data, status=status.HTTP_200_OK)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        body = request.body
        try:
            data = json.loads(body.decode('utf-8'))
        except ValueError:
            return Response(data={"msg": "非合法json格式"}, status=status.HTTP_404_NOT_FOUND)

        wh_id = data.get('wh_id')
        obj = self.get_object(pk=wh_id)
        if not obj:
            return Response(data={"msg": "没有此仓库信息"}, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderList(APIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = FreshPagination

    def get(self, request):
        """
        Get all list.
        :param request:
        :return:
        """
        queryset = OrderInfo.objects.all()
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            s = OrderInfoSerializer(instance=page, many=True)
            return paginator.get_paginated_response(s.data)

        s = OrderInfoSerializer(instance=queryset, many=True)
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Post a new record.
        :param request:
        :return:
        """
        s = OrderInfoSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetail(APIView):
    @staticmethod
    def get_object(pk):
        """
        Get object according to given primary key.
        :param pk:
        :return:
        """
        try:
            return OrderInfo.objects.get(pk=pk)
        except:
            return

    def get(self, request):
        """
        查询id、近7天的订单
        :param request:
        :return:
        """
        func = request.GET.get('function')
        if func == "id":
            order_id = request.GET.get('order_id')
            obj = self.get_object(pk=order_id)
            if not obj:
                return Response(data={"msg": "没有此订单信息"}, status=status.HTTP_404_NOT_FOUND)
            s = OrderInfoSerializer(instance=obj)
            return Response(s.data, status=status.HTTP_200_OK)

        #查询最近7天的订单
        if func == "latest":
            today = date.today()
            one_week_ago = today - timedelta(days=7)

            obj = OrderInfo.objects.filter(
                order_time__gte=one_week_ago
            )
            if not obj:
                return Response(data={"msg": "最近7天没有订单信息"}, status=status.HTTP_404_NOT_FOUND)
            s = OrderInfoSerializer(instance=obj)
            return Response(s.data, status=status.HTTP_200_OK)

    def put(self, request):
        """

        :param request:
        :param pk:
        :return:
        """
        body = request.body
        try:
            data = json.loads(body.decode('utf-8'))
        except ValueError:
            return Response(data={"msg": "非合法json格式"}, status=status.HTTP_404_NOT_FOUND)

        order_id = data.get('order_id')
        obj = self.get_object(pk=order_id)
        if not obj:
            return Response(data={"msg": "没有此订单信息"}, status=status.HTTP_404_NOT_FOUND)
        s = OrderInfoSerializer(instance=obj, data=request.data)
        if s.is_valid():
            s.save()
            return Response(data=s.data, status=status.HTTP_200_OK)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        """
        Delete objects according to order_id.
        :param request:
        :param pk:
        :return:
        """
        body = request.body
        try:
            data = json.loads(body.decode('utf-8'))
        except ValueError:
            return Response(data={"msg": "非合法json格式"}, status=status.HTTP_404_NOT_FOUND)

        order_id = data.get('order_id')
        obj = self.get_object(pk=order_id)
        if not obj:
            return Response(data={"msg": "没有此订单信息"}, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BuyList(APIView):
    def get(self, request):
        queryset = BuyRecord.objects.all()
        s = BuyRecordSerializer(instance=queryset, many=True)
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self, request):
        s = BuyRecordSerializer(data=request.data)
        if s.is_valid():
            print(s)
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


class BuyDetail(APIView):
    def get(self, request):
        """
        查询近一周内要过期、某一类型的货物采购记录
        :param request:
        :return:
        """
        func = request.GET.get('function')

        # 查询近一周内要过期的货物
        if func == 'neardue':
            today = date.today()
            one_week_later = today + timedelta(days=7)

            days = ExpressionWrapper(F('g__g_life'), output_field=DurationField())
            obj = BuyRecord.objects.filter(
                buy_pdate__lte=one_week_later - days
            )
            if not obj:
                return Response(data={"msg": "没有此货物信息"}, status=status.HTTP_404_NOT_FOUND)
            s = BuyRecordSerializer(instance=obj, many=True)
            return Response(s.data, status=status.HTTP_200_OK)

        # 查询某一类型货物的采购信息（蔬菜、肉类、乳制品等）
        if func == "type":
            goods_type = request.GET.get("goods_type")
            obj = BuyRecord.objects.filter(
                g__g_category__exact=goods_type
            )
            if not obj:
                return Response(data={"msg": "没有此货物信息"}, status=status.HTTP_404_NOT_FOUND)
            s = BuyRecordSerializer(instance=obj, many=True)
            return Response(s.data, status=status.HTTP_200_OK)


class OutboundList(APIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = FreshPagination

    def get(self, request):
        """
        返回所有数据
        :param request:
        :return:
        """
        queryset = OutboundRecord.objects.all()
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            s = OutboundRecordSerializer(instance=page, many=True)
            return paginator.get_paginated_response(s.data)

        s = OutboundRecordSerializer(instance=queryset, many=True)
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        新增一条数据
        :param request:
        :return:
        """
        s = OutboundRecordSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


class OutboundDetail(APIView):
    @staticmethod
    def get_object(pk):
        """
        Get object according to given primary key.
        :param pk:
        :return:
        """
        try:
            return OrderInfo.objects.get(pk=pk)
        except:
            return

    def get(self, request):
        """
        查询id或者近7天的出库记录
        :param request:
        :return:
        """
        func = request.GET.get('function')
        obj = None
        #按照id查询出库记录
        if func == "id":
            outbound_id = request.GET.get('outbound_id')
            obj = self.get_object(pk=outbound_id)
            if not obj:
                return Response(data={"msg": "没有此出库记录"}, status=status.HTTP_404_NOT_FOUND)

        #查询最近7天的出库记录
        if func == "latest":
            today = date.today()
            one_week_ago = today - timedelta(days=7)
            obj = OutboundRecord.objects.filter(
                out_time__gte=one_week_ago
            )
            if not obj:
                return Response(data={"msg": "最近7天没有出库记录"}, status=status.HTTP_404_NOT_FOUND)

        s = OutboundRecordSerializer(instance=obj, many=True)
        return Response(s.data, status=status.HTTP_200_OK)


class TransportationList(APIView):
    def get(self, request):
        queryset = TransportationInfo.objects.all()
        s = TransportationInfoSerializer(instance=queryset, many=True)
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self, request):
        s = TransportationInfoSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


class TransportList(APIView):
    def get(self, request):
        queryset = TransportRecord.objects.all()
        s = TransportRecordSerializer(instance=queryset, many=True)
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self, request):
        s = TransportRecordSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


class TransportDetail(APIView):
    def get(self, request):
        func = request.GET.get('function')
        queryset = None
        if func == "loc":
            loc = request.GET.get('loc')
            queryset = TransportRecord.objects.filter(transport_to__contains=loc)
            if not queryset:
                return Response(data={'msg': "没有送往此地的记录"}, status=status.HTTP_404_NOT_FOUND)

        if func == "id":
            t_id = request.GET.get('id')
            queryset = TransportRecord.objects.filter(transportation_id=t_id)
            if not queryset:
                return Response(data={'msg': "没有此车的运输记录"}, status=status.HTTP_404_NOT_FOUND)

        s = TransportRecordSerializer(instance=queryset, many=True)
        return Response(s.data, status=status.HTTP_200_OK)


class TransferList(APIView):
    def get(self, request):
        queryset = TransferInfo.objects.all()
        s = TransferInfoSerializer(instance=queryset, many=True)
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self, request):
        s = TransferInfoSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


class StockList(APIView):
    def get(self, request):
        queryset = TransferInfo.objects.all()
        s = TransferInfoSerializer(instance=queryset, many=True)
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self, request):
        s = StockInfoSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
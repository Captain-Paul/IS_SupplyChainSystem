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


class FreshPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class GoodsList(APIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = FreshPagination

    def get(self, request):
        """

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
        queryset = WarehouseInfo.objects.all()
        s = WarehouseInfoSerializer(instance=queryset, many=True)
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self, request):
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
        wh_id = request.GET.get('wh_id')
        obj = self.get_object(pk=wh_id)
        if not obj:
            return Response(data={"msg": "没有此仓库信息"}, status=status.HTTP_404_NOT_FOUND)
        s = WarehouseInfoSerializer(instance=obj)
        return Response(s.data, status=status.HTTP_200_OK)

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
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


class BuyDetail(APIView):
    def get(self, request):
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
from rest_framework import serializers
from .models import *
from django import forms
from django.contrib.auth.models import User


class StaffInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = StaffInfo
        fields = "__all__"

class KpiInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = KpiInfo
        fields = "__all__"

class GoodsInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodsInfo
        fields = "__all__"

class WarehouseInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = WarehouseInfo
        fields = "__all__"

class BuyRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = BuyRecord
        fields = "__all__"

class CountRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = CountRecord
        fields = "__all__"

class OrderInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderInfo
        fields = "__all__"

class OutboundRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = OutboundRecord
        fields = "__all__"

class StockInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = StockInfo
        fields = "__all__"

class TransportationInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TransportationInfo
        fields = "__all__"

class TransportRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = TransportRecord
        fields = "__all__"

class TransferInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TransferInfo
        fields = "__all__"
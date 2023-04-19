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
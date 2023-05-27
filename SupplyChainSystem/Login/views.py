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

class LoginView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        # 获取用户输入的id和password
        try:
            s_id = request.GET.get('id')
            s_pw = request.GET.get('pw')
        except:
            return Response('用户名不能为空.')

        # 检测用户是否存在
        try:
            staff = StaffInfo.objects.get(pk=s_id)
            # 检测密码是否正确
            try:
                staff_pwright = StaffInfo.objects.get(pk=s_id, s_pw=s_pw)
            except:
                return Response('密码错误')
        except:
            return Response('用户不存在')

        # try:
        #     staff = StaffInfo.object.get(Ls_id=id, Ls_pw=password)
        # except StaffInfo.DoesNotExist:
        #     return Response('用户不存在或密码错误.')
        ## 返回用户信息
        # s = StaffInfoSerializer(instance=staff, many=False)
        # return Response(s.data, status=status.HTTP_200_OK)
        return Response({"message":"登陆成功", "id":s_id, "pw":s_pw})

class RegisterView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        s_id = request.GET.get('s_id')

        # 检查 s_id 是否已经在数据库中存在
        if StaffInfo.objects.filter(s_id=s_id).exists():
            return Response({'message': '该员工号已存在'}, status=status.HTTP_400_BAD_REQUEST)

        # 添加新员工信息到数据库
        s = StaffInfoSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response({'message': '员工信息添加成功'}, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

# class LoginView(APIView):
#     def get(self, request):
#         form = MyAuthenticationForm()
#         return render(request, 'login.html', {'form': form})
#
#     def post(self, request):
#         form = MyAuthenticationForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#         return render(request, 'login.html', {'form': form})

class StaffPagination(PageNumberPagination):
    '''
    分页属性
    '''
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class StaffList(APIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = StaffPagination

    def get(self, request):
        queryset = StaffInfo.objects.all()
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            s = StaffInfoSerializer(instance=page, many=True)
            return paginator.get_paginated_response(s.data)

        s = StaffInfoSerializer(instance=queryset, many=True)
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self, request):
        pass

class StaffDetail(APIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = StaffPagination

    def get(self, request):
        pass
    def post(self, request):
        pass

class KPIList(APIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = StaffPagination

    def get(self, request):
        queryset = KPIInfo.objects.all()
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            s = KPIInfoSerializer(instance=page, many=True)
            return paginator.get_paginated_response(s.data)

        s = KPIInfoSerializer(instance=queryset, many=True)
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self, request):
        pass

class KPIDetail(APIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = StaffPagination

    def get(self, request):
        pass
    def post(self, request):
        pass

from django.shortcuts import render

from django.db.models.signals import post_save
from django.db.models import Q, F, ExpressionWrapper, Func
from django.db.models.fields import DurationField
from django.contrib.auth.models import User, Group
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
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import *
from .models import *
from .serializers import *
import json
from datetime import date, timedelta


class LoginView(APIView):
    authentication_classes = [BasicAuthentication]

    # permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user_username = request.GET.get('username')
            password = request.GET.get('pw')
            role_name = request.GET.get('role')
            if not user_username or not password or not role_name:
                return Response('用户名、密码和部门不能为空.')
        except:
            return Response('请求参数不正确.')

        # 检查部门和用户是否存在并验证密码
        try:
            group = Group.objects.get(name=role_name)
            user = User.objects.get(username=user_username, groups=group)
            if not user.check_password(password):
                return Response('密码错误.')
        except Group.DoesNotExist:
            return Response('指定的部门不存在.')
        except User.DoesNotExist:
            return Response('指定的用户不存在.')

        # 创建或获取用户的 Token
        token, created = Token.objects.get_or_create(user=user)

        # 处理验证成功的用户记录
        # ...

        # 将 Token 添加到响应头中返回
        response = Response('登录成功.')
        response['Authorization'] = f'Token {token.key}'
        return response


# class RegisterView(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def get(self, request):
#         s_id = request.GET.get('s_id')
#
#         # 检查 s_id 是否已经在数据库中存在
#         if StaffInfo.objects.filter(s_id=s_id).exists():
#             return Response({'message': '该员工号已存在'}, status=status.HTTP_400_BAD_REQUEST)
#
#         # 添加新员工信息到数据库
#         s = StaffInfoSerializer(data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response({'message': '员工信息添加成功'}, status=status.HTTP_201_CREATED)
#         return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


class StaffPagination(PageNumberPagination):
    """
    分页属性
    """
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class StaffList(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated, StaffListPermission,)
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
    #
    # def post(self, request):
    #     s = StaffInfoSerializer(data=request.data)
    #     if s.is_valid():
    #         s.save()
    #         return Response(s.data, status=status.HTTP_201_CREATED)
    #     return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


class StaffDetail(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated, StaffDetailPermission)
    pagination_class = StaffPagination

    @staticmethod
    def get_object(pk):
        """
        Get object according to given primary key.
        :param pk: primary key
        :return:
        """
        try:
            return StaffInfo.objects.get(pk=pk)
        except:
            return

    def get(self, request):
        """
        带参数查询
        :param request:
        :return:
        """
        func = request.GET.get('function')

        if not func:
            return Response(data={"msg": "需要function参数"})
        elif func == 'id':
            obj = self.get_object(request.GET.get('s_id'))
            if not obj:
                return Response(data={"msg": "没有员工信息"}, status=status.HTTP_404_NOT_FOUND)
            s = StaffInfoSerializer(instance=obj)
            return Response(s.data, status=status.HTTP_200_OK)

    # def put(self, request):
    #     """
    #     更新一条数据
    #     :param request:
    #     :return:
    #     """
    #     body = request.body
    #     try:
    #         data = json.loads(body.decode('utf-8'))
    #     except ValueError:
    #         return Response(data={"msg": "非合法json格式"}, status=status.HTTP_404_NOT_FOUND)
    #
    #     s_id = data.get('s_id')
    #     obj = self.get_object(s_id)
    #     if not obj:
    #         return Response(data={"msg": "没有此员工信息"}, status=status.HTTP_404_NOT_FOUND)
    #     s = StaffInfoSerializer(instance=obj, data=request.data)
    #     if s.is_valid():
    #         s.save()
    #         return Response(data=s.data, status=status.HTTP_200_OK)
    #     return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request):
    #     """
    #     删除一条数据
    #     :param request:
    #     :return:
    #     """
    #     body = request.body
    #     try:
    #         data = json.loads(body.decode('utf-8'))
    #     except ValueError:
    #         return Response(data={"msg": "非合法json格式"}, status=status.HTTP_404_NOT_FOUND)
    #
    #     s_id = data.get('s_id')
    #     obj = self.get_object(pk=s_id)
    #     if not obj:
    #         return Response(data={"msg": "没有此员工信息"}, status=status.HTTP_404_NOT_FOUND)
    #     obj.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class KpiList(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated, KpiListPermission)
    pagination_class = StaffPagination

    def get(self, request):
        queryset = KpiInfo.objects.all()
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            s = KpiInfoSerializer(instance=page, many=True)
            return paginator.get_paginated_response(s.data)

        s = KpiInfoSerializer(instance=queryset, many=True)
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        添加一条kpi信息
        :param request:
        :return:
        """
        s = KpiInfoSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


class KpiDetail(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated, KpiDetailPermission)
    pagination_class = StaffPagination

    @staticmethod
    def get_object(pk):
        """
        Get object according to given primary key.
        :param pk: primary key
        :return:
        """
        try:
            return KpiInfo.objects.get(pk=pk)
        except:
            return

    def get(self, request):
        """
        带参数查询
        :param request:
        :return:
        """
        func = request.GET.get('function')

        if not func:
            return Response(data={"msg": "需要function参数"})
        elif func == 'id':
            obj = self.get_object(request.GET.get('k_id'))
            if not obj:
                return Response(data={"msg": "没有KPI信息"}, status=status.HTTP_404_NOT_FOUND)
            s = KpiInfoSerializer(instance=obj)
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

        k_id = data.get('k_id')
        obj = self.get_object(pk=k_id)
        if not obj:
            return Response(data={"msg": "没有此KPI信息"}, status=status.HTTP_404_NOT_FOUND)
        s = KpiInfoSerializer(instance=obj, data=request.data)
        if s.is_valid():
            s.save()
            return Response(data=s.data, status=status.HTTP_200_OK)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        """
        删除一条数据
        :param request:
        :return:
        """
        body = request.body
        try:
            data = json.loads(body.decode('utf-8'))
        except ValueError:
            return Response(data={"msg": "非合法json格式"}, status=status.HTTP_404_NOT_FOUND)

        k_id = data.get('k_id')
        obj = self.get_object(pk=k_id)
        if not obj:
            return Response(data={"msg": "没有此KPI信息"}, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

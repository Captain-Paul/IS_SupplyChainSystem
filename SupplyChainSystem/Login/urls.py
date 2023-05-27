from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Login import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name="register"),
    path('login/', views.LoginView.as_view(), name="login"),

    path('list/', views.StaffList.as_view(), name="staff-list"),
    path('detail/', views.StaffDetail.as_view(), name="staff-detail"),

    path('KPI/list/', views.KPIList.as_view(), name="KPI-list"),
    path('KPI/detail/', views.KPIDetail.as_view(), name="KPI-detail")
]

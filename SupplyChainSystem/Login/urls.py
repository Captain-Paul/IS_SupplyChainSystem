from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Login import views

urlpatterns = [
    # path('register/', views.RegisterView.as_view(), name="register"),
    path('login/', views.LoginView.as_view(), name="login"),

    path('staff/list/', views.StaffList.as_view(), name="staff-list"),
    path('staff/detail/', views.StaffDetail.as_view(), name="staff-detail"),

    path('KPI/list/', views.KpiList.as_view(), name="KPI-list"),
    path('KPI/detail/', views.KpiDetail.as_view(), name="KPI-detail")
]

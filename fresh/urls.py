from django.urls import path, include
from rest_framework.routers import DefaultRouter
from fresh import views

# router = DefaultRouter()
# router.register(prefix="viewsets", viewset=views.CourseViewSet)

urlpatterns = [
    path("goods/list/", views.GoodsList.as_view(), name="goods-list"),
    path("goods/detail/", views.GoodsDetail.as_view(), name="goods-detail"),
    path("order/list/", views.OrderList.as_view(), name="order-list"),
    path("order/detail/", views.OrderDetail.as_view(), name="order-detail")
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from fresh import views

# router = DefaultRouter()
# router.register(prefix="viewsets", viewset=views.CourseViewSet)

urlpatterns = [
    path("goods/list/", views.GoodsList.as_view(), name="goods-list"),
    path("goods/detail/", views.GoodsDetail.as_view(), name="goods-detail"),
    path("warehouse/list/", views.WarehouseList.as_view(), name="warehouse-list"),
    path("warehouse/detail/", views.WarehouseDetail.as_view(), name="warehouse-detail"),
    path("order/list/", views.OrderList.as_view(), name="order-list"),
    path("order/detail/", views.OrderDetail.as_view(), name="order-detail"),
    path("buy/list/", views.BuyList.as_view(), name="buy-list"),
    path("buy/detail/", views.BuyDetail.as_view(), name="buy-detail")
]
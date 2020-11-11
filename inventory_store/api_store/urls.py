from django.urls import path
from .api import ProductList, BatchList, OrderList, BatchDetail

urlpatterns = [
    path("products/", ProductList.as_view(), name="product_list"),
    path("batch_list/", BatchList.as_view(), name="batch_list"),
    path("order_list/", OrderList.as_view(), name="order_list"),
    path("batch_detail/<int:pk>/", BatchDetail.as_view(), name="batch_detail"),
]

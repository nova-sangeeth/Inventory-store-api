from django.urls import path
from .api import ProductList, BatchList, OrderList, BatchDetail, ExpiredProducts, FreshProducts, ExpiringProducts

urlpatterns = [
    path("products/", ProductList.as_view(), name="product_list"),
    path("batch_list/", BatchList.as_view(), name="batch_list"),
    path("order_list/", OrderList.as_view(), name="order_list"),
    path("batch_detail/<int:pk>/", BatchDetail.as_view(), name="batch_detail"),
    path("expired/", ExpiredProducts.as_view(), name="expired"),
    path("fresh_products", FreshProducts.as_view(), name='fresh_products'),
    path("expiring_products", ExpiringProducts.as_view(), name="expiring_products")
]

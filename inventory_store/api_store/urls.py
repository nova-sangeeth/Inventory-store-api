from django.urls import path
from .api import ProductList, BatchList

urlpatterns = [
        path("products/", ProductList.as_view(), name="product_list"),
        path("batch_list/", BatchList.as_view(), name="batch_list"),
        ]



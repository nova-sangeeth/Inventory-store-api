from django.urls import path
from .api import ProductList

urlpatterns = [
        path("products/", ProductList.as_view(), name="product_list"),
        ]



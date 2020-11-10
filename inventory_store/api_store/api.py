from rest_framework import generics
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import Product
from .serializer import productSerializer
import datetime

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = productSerializer


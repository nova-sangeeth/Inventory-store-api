from rest_framework import generics
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import Product, Batch, Order
from .serializer import productSerializer, batchSerializer, orderSerializer
import datetime


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = productSerializer


class BatchList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Batch.objects.all()
    serializer_class = batchSerializer


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = orderSerializer


class BatchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Batch.objects.all()
    serializer_class = batchSerializer

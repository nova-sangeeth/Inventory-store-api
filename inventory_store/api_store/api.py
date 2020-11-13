from datetime import date
from rest_framework import generics
from rest_framework import serializers
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


class ExpiredProducts(generics.ListCreateAPIView):
    queryset = Batch.objects.filter(expiry_date__lt=date.today())
    serializer_class = batchSerializer

class FreshProducts(generics.ListCreateAPIView):
    queryset = Batch.objects.filter(expiry_date__gt=date.today())
    # queryset = Batch.objects.filter(expiry_date__gt=date.today()+datetime(days=3))
    serializer_class = batchSerializer

class ExpiringProducts(generics.ListAPIView):
    queryset = Batch.objects.filter(expiry_date__lte=date.today()+datetime.timedelta(days=3))
    # queryset = Batch.objects.filter(expiry_date__lte=date.today()+datetime.timedelta(days=3)).exclude(expiry_date__lt =date.today())
    serializer_class = batchSerializer

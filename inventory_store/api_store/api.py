from rest_framework import generics
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import Product, Batch
from .serializer import productSerializer, batchSerializer
import datetime

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = productSerializer

class BatchList(generics.ListCreateAPIView):
    queryset = Batch.objects.all()
    serializer_class = batchSerializer

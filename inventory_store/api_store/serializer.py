from django.db.models import fields
from rest_framework import serializers
from .models import Product, Batch

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class batchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'





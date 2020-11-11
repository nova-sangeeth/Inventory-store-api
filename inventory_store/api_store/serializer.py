from django.db.models import fields
from rest_framework import serializers
from .models import Order, Product, Batch


class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class batchSerializer(serializers.ModelSerializer):
    batch_in_order = orderSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Batch
        fields = '__all__'


class productSerializer(serializers.ModelSerializer):
    batch_in_order = batchSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Product
        fields = '__all__'

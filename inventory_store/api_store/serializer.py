from django.db.models import fields
from rest_framework import serializers
from .models import Order, Product, Batch, sale_details


class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ('date_added',)


class batchSerializer(serializers.ModelSerializer):
    batch_in_order = orderSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Batch
        exclude = ('date_added',)


class productSerializer(serializers.ModelSerializer):
    batch_in_order = batchSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Product
        exclude = ('date_added',)


class saleSerializer(serializers.ModelSerializer):
    class Meta:
        model = sale_details
        exclude = ('date_added',)

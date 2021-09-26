from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('image', 'name', 'description', 'price')
        read_only_fields = ('id',)
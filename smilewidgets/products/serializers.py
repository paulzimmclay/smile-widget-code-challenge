from rest_framework import serializers
from .models import ProductPrice


class ProductPriceSerializer(serializers.Serializer):
    class Meta:
        model = ProductPrice
        fields = ('code', 'price', 'date_start', 'date_end')

class ProductSerializer(serializers.Serializer):
    class Meta:
        model = ProductPrice
        fields = ('name', 'code', 'price')
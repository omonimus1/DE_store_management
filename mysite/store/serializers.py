from rest_framework import serializers

from .models import Product, User, ProductImage

class ProductSerializer(serializers.HyperlinkModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price')
    
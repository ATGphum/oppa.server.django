# serializers.py

from rest_framework import serializers

from .models import Product

# serialize models here

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'imageUrl', 'miscimageUrl', 'price', 'stock', 'description', 'branddescription')
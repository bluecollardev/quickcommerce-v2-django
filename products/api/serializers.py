from rest_framework import serializers
from products.models import Product

class productSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('pk', 'name', 'price', 'description')
from rest_framework import serializers
from quickcommerce.models import Product
from quickcommerce.models import Customer

class productSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('pk', 'name', 'price', 'description')

class customerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('pk', 'firstname', 'middlename', 'lastname', 'email', 'phone', 'description')
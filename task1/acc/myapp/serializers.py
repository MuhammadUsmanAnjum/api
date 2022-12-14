from rest_framework import serializers
from .models import *


class ShopDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopDetail
        # fields = '__all__'
        fields = ('id', 'shop_name')

class SupplierInfoSerializer(serializers.ModelSerializer):
    shops_detail = ShopDetailSerializer(many=True)
    class Meta:
        model = SupplierInfo
        fields = ('supplier_name', 'address','shops_detail')
        # fields = '__all__'






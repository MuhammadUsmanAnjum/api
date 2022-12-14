from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import SupplierInfoSerializer, ShopDetailSerializer
from .models import SupplierInfo, ShopDetail
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework import filters

# Create your views here.

class SupplierInfoViewSet(ListAPIView):
#     # def list(self, request):
#     #     queryset = SupplierInfo.objects.all()
#     #     serializer = SupplierInfoSerializer(queryset, many=True)
#     #     return Response(serializer.data)

    queryset=SupplierInfo.objects.all()
    serializer_class=SupplierInfoSerializer



class ShopDetailViewSet(ListAPIView):
    queryset=ShopDetail.objects.all()
    serializer_class=ShopDetailSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['shop_name']





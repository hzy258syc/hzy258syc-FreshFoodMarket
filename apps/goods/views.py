from django.shortcuts import render
from rest_framework.views import APIView
from goods.serializers import GoodsSerializer
from .models import Goods
from rest_framework import serializers,mixins,generics,settings
from rest_framework.response import Response
# Create your views here.


# class GoodsListView(APIView):
#     """
#     商品列表
#     """
#     def get(self, request, format=None):
#         goods = Goods.objects.all()
#         goods_serialzer = GoodsSerializer(goods, many=True)
#         print(1111)
#         return Response(goods_serialzer.data)


class GoodsListView(generics.ListAPIView):
    '商品列表页'
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

    # def get(self,request,*args,**kwargs):
    #     return self.list(request,*args,**kwargs)

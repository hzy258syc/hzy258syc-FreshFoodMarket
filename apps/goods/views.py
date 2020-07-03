from django.shortcuts import render
from rest_framework.views import APIView
from goods.serializers import GoodsSerializer
from .models import Goods
from rest_framework import serializers,mixins,generics,viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
# Create your views here.


class GoodsPagination(PageNumberPagination):
    """
    商品列表自定义分页
    """
    # 默认每页显示的个数
    page_size = 10
    # 可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    # 页码参数
    page_query_param = 'page'
    # 最多能显示多少页
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表页
    """
    pagination_class = GoodsPagination
    # 这里必须定义一个默认的排序，否则会报错
    queryset = Goods.objects.all().order_by('id')
    serializer_class = GoodsSerializer



# class GoodsListView(generics.ListAPIView):
#     '商品列表页'
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#
#     # def get(self,request,*args,**kwargs):
#     #     return self.list(request,*args,**kwargs)

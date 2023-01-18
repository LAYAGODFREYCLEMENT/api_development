from django.shortcuts import render
from rest_framework.generics import ListAPIView
from products.serializers import ProductCategorySerializer
from products.models import ProductCategory, Maker, Product


class ProductCategoryListView(ListAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()

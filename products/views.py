from django.shortcuts import render
from rest_framework.generics import ListAPIView
from products.serializers import ProductCategorySerializer, MakerSerializer
from products.models import ProductCategory, Maker, Product


class ProductCategoryListView(ListAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()


class MakerListView(ListAPIView):
    serializer_class = Maker
    queryset = Maker.objects.all()

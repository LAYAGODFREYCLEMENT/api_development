from django.shortcuts import render
from rest_framework.generics import ListAPIView
from products.serializers import ProductCategorySerializer, MakerSerializer
from products.models import ProductCategory, Maker, Product


class ProductCategoryListView(ListAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()


class MakerListView(ListAPIView):
    class Meta:
        serializer_class = Maker
        querySet = Maker.objects.all()

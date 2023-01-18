from rest_framework import serializers
from products.models import ProductCategory, Maker, Product


class ProductCategoryListView(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"

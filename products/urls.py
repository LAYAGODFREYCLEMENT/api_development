from django.urls import path, include
from products.views import ProductCategoryListView

app_name = "products"

urlpatterns = [
    path("categories/", ProductCategoryListView.as_view(), name="categories-list"),
]

from django.urls import path, include
from products.views import ProductCategoryListView, MakerListView, ProductListView

app_name = "products"

urlpatterns = [
    path("", ProductListView.as_view(), name="maker-list"),
    path("categories/", ProductCategoryListView.as_view(), name="categories-list"),
    path("makers/", MakerListView.as_view(), name="maker-list"),
]

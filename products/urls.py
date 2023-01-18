from django.urls import path, include
from products.views import ProductCategoryListView, MakerListView

app_name = "products"

urlpatterns = [
    path("categories/", ProductCategoryListView.as_view(), name="categories-list"),
    path("maker/", MakerListView.as_view(), name="maker-list"),
]

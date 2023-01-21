from django.urls import include, path

from products.views import MakerListView, ProductCategoryListView, ProductListView

app_name = "products"

urlpatterns = [
    path("", ProductListView.as_view(), name="maker-list"),
    path("categories/", ProductCategoryListView.as_view(), name="categories-list"),
    path("makers/", MakerListView.as_view(), name="maker-list"),
]

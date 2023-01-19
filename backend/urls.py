from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("products/", include("products.urls", namespace="products")),
    path("auth/", include("authTokens.urls", namespace="authTokens")),
]

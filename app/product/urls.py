from django.urls import path, include

from rest_framework.routers import DefaultRouter
from product import views

router = DefaultRouter()
router.register(r"category", views.CategoryViewSet)
router.register(r"brand", views.BrandViewSet)
router.register(r"product", views.ProductViewSet, basename="products")

app_name = "product"

urlpatterns = [
    path("", include(router.urls)),
]

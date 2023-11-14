from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from product.models import Category, Brand, Product
from product import serializers


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Category list"""

    lookup_field = "name"
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class BrandViewSet(viewsets.ReadOnlyModelViewSet):
    """Brand list"""

    lookup_field = "name"
    queryset = Brand.objects.all()
    serializer_class = serializers.BrandSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """Product list"""

    lookup_field = "name"
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category__name", "brand__name"]

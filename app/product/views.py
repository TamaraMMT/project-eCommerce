from rest_framework import viewsets
from product.models import Category, Brand, Product
from product import serializers


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Category list"""

    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class BrandViewSet(viewsets.ReadOnlyModelViewSet):
    """Brand list"""

    queryset = Brand.objects.all()
    serializer_class = serializers.BrandSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """Product list"""

    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer

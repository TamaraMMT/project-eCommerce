from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter,
    OpenApiTypes,
)
from django.db.models import Prefetch

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from product.models import Category, Brand, Product
from product import serializers


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Category list"""

    lookup_field = "name"
    queryset = Category.objects.filter(is_active=True)
    serializer_class = serializers.CategorySerializer


class BrandViewSet(viewsets.ReadOnlyModelViewSet):
    """Brand list"""

    lookup_field = "name"
    queryset = Brand.objects.filter(is_active=True)
    serializer_class = serializers.BrandSerializer


@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                "category__name",
                OpenApiTypes.STR,
                description="Input the category name to filter",
            ),
            OpenApiParameter(
                "brand__name",
                OpenApiTypes.STR,
                description="Input the brand name to filter",
            ),
        ]
    )
)
class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """Products"""

    lookup_field = "name"
    serializer_class = serializers.ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category__name", "brand__name"]

    def get_queryset(self):
        return (
            Product.objects.filter(is_active=True)
            .select_related("category", "brand")
            .prefetch_related(
                Prefetch("product_line__product_image"),
            )
        )

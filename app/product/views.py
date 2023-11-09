from rest_framework import viewsets
from product.models import Category
from product.serializers import CategorySerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Category list"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from product.models import Product
from product.serializers import ProductSerializer
from users.permissions import IsActiveEmployee


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveEmployee]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name", "model", "release_date"]

    def get_queryset(self):
        return Product.objects.select_related("network_node")

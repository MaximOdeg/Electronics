from rest_framework import permissions, viewsets

from .models import NetworkNode, Supplier
from .serializers import NetworkNodeSerializer, SupplierSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [permissions.IsAuthenticated]


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(debt_to_supplier=self.get_object().debt_to_supplier)

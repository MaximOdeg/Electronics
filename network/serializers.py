from rest_framework import serializers

from .models import NetworkNode, Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"
        read_only_fields = ["debt"]


class NetworkNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkNode
        fields = "__all__"

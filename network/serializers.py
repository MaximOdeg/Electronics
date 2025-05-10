from rest_framework import serializers

from network.models import NetworkNode
from product.serializers import ProductSerializer


class NetworkNodeSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True, default=[])

    class Meta:
        model = NetworkNode
        fields = "__all__"
        read_only_fields = ("debt", "created_at")

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import NetworkNodeViewSet, SupplierViewSet

router = DefaultRouter()
router.register(r"network-nodes", NetworkNodeViewSet)
router.register(r"products", SupplierViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]

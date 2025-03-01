from django.urls import include, path
from rest_framework.routers import SimpleRouter

from network.apps import NetworkConfig
from network.views import NetworkNodeViewSet

app_name = NetworkConfig.name

router = SimpleRouter()
router.register(r"nodes", NetworkNodeViewSet, basename="nodes")

urlpatterns = [
    path("", include(router.urls)),
]

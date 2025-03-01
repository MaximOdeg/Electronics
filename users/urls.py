from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import CustomUserCreateAPIView, CustomUserViewSet

app_name = UsersConfig.name

router = SimpleRouter()
router.register("", CustomUserViewSet, basename="user")

urlpatterns = [
    path("api/register/", CustomUserCreateAPIView.as_view(), name="register"),
    path(
        "api/login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path("api/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns += router.urls

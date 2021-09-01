from django.urls import path
from django.urls.conf import include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("/users", include(("users.urls", "users"))),
    path("/auth/token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("/auth/token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
]

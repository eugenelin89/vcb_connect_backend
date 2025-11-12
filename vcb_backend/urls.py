from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from accounts.urls import router as accounts_router
from games.urls import router as games_router
from leagues.urls import router as leagues_router
from points.urls import router as points_router
from shop.urls import router as shop_router
from volunteers.urls import router as volunteers_router

router = DefaultRouter()
for r in (
    accounts_router,
    leagues_router,
    volunteers_router,
    games_router,
    shop_router,
    points_router,
):
    router.registry.extend(r.registry)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("rest_framework.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("api/", include(router.urls)),
]

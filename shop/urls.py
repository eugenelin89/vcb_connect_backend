from rest_framework.routers import DefaultRouter
from .views import PlaceholderViewSet


router = DefaultRouter()
router.register(r"shop", PlaceholderViewSet, basename="shop")

urlpatterns = router.urls

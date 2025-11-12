from rest_framework.routers import DefaultRouter
from .views import PlaceholderViewSet


router = DefaultRouter()
router.register(r"leagues", PlaceholderViewSet, basename="leagues")

urlpatterns = router.urls

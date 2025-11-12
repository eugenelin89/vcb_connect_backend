from rest_framework.routers import DefaultRouter
from .views import PlaceholderViewSet


router = DefaultRouter()
router.register(r"points", PlaceholderViewSet, basename="points")

urlpatterns = router.urls

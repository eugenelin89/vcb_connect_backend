from rest_framework.routers import DefaultRouter
from .views import PlaceholderViewSet


router = DefaultRouter()
router.register(r"volunteers", PlaceholderViewSet, basename="volunteers")

urlpatterns = router.urls

from rest_framework.routers import DefaultRouter
from .views import PlaceholderViewSet


router = DefaultRouter()
router.register(r"games", PlaceholderViewSet, basename="games")

urlpatterns = router.urls

from rest_framework.routers import DefaultRouter
from .views import PlaceholderViewSet


router = DefaultRouter()
router.register(r"accounts", PlaceholderViewSet, basename="accounts")

urlpatterns = router.urls

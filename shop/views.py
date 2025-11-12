from rest_framework import response, viewsets
from .serializers import PlaceholderSerializer


class PlaceholderViewSet(viewsets.ViewSet):
    """Placeholder endpoint until real models exist."""

    def list(self, request):
        serializer = PlaceholderSerializer({'message': "Shop endpoint coming soon"})
        return response.Response(serializer.data)

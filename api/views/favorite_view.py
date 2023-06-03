from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from api.serializers.favorite_serializer import FavoriteSerializer


class BooksFavoriteView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FavoriteSerializer

from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from api.serializers.review_serializer import ReviewCreateSerializer


class ReviewCreateApiView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewCreateSerializer

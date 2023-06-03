from rest_framework.generics import CreateAPIView
from api.serializers.review_serializer import ReviewCreateSerializer


class ReviewCreateApiView(CreateAPIView):
    serializer_class = ReviewCreateSerializer

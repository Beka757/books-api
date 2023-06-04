from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated

from api.serializers.review_serializer import ReviewCreateSerializer
from app.models import Book


class ReviewCreateApiView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewCreateSerializer

    def perform_create(self, serializer):
        book = get_object_or_404(Book, pk=self.kwargs['pk'])
        serializer.save(book=book, user=self.request.user)

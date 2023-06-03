from rest_framework.generics import ListAPIView
from api.serializers.book_serializer import BooksSerializer
from api.services.book_services import BookService
from django_filters.rest_framework import DjangoFilterBackend
from api.serializers.book_serializer import BookFilter


class BookListApiView(ListAPIView):
    serializer_class = BooksSerializer
    queryset = BookService.get_books()
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter

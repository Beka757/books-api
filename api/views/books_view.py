from rest_framework.generics import ListAPIView, RetrieveAPIView
from api.serializers.book_serializer import BooksSerializer, BookFilter, BookDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend

from app.models import Book


class BookListApiView(ListAPIView):
    serializer_class = BooksSerializer
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter


class BookDetailApiView(RetrieveAPIView):
    serializer_class = BookDetailSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Book.objects.filter(id=self.kwargs['id'])

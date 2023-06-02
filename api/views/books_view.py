from rest_framework.generics import ListAPIView
from api.serializers.book_serializer import BooksSerializer
from app.models.book import Book
from api.services.book_services import BookService


class BookListApiView(ListAPIView):
    model = Book
    serializer_class = BooksSerializer
    queryset = BookService.get_books()

from app.models.book import Book


class BookService:
    @staticmethod
    def get_books():
        return Book.objects.all()

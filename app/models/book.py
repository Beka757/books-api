from django.db import models
from .author import Author
from .genre import Genre
from django.db.models import Avg


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=500, verbose_name='Описание')
    publication_date = models.DateField(verbose_name='Дата публикации')
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='author_books', verbose_name='Автор')
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='genre_books', verbose_name='Жанр')

    def average_rating(self):
        average_rating = self.book_reviews.aggregate(avg_rating=Avg('rating')).get('avg_rating')
        return average_rating or None

    def get_reviews(self):
        return self.book_reviews.all()

    def __str__(self):
        return self.title

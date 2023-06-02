from django.contrib.auth import get_user_model
from django.db import models
from .book import Book


class Review(models.Model):
    user_id = models.ForeignKey(get_user_model(), related_name='user_reviews', on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, related_name='book_reviews', on_delete=models.CASCADE)
    text = models.TextField(max_length=2000, verbose_name='Отзыв')

    def __str__(self):
        return self.text

from django.contrib.auth import get_user_model
from django.db import models
from .book import Book


class Favorite(models.Model):
    user_id = models.ForeignKey(get_user_model(), related_name='user_favorites', on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, related_name='book_favorites', on_delete=models.CASCADE)

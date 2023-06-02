from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .book import Book


class Rating(models.Model):
    user_id = models.ForeignKey(get_user_model(), related_name='user_ratings', on_delete=models.PROTECT)
    book_id = models.ForeignKey(Book, related_name='book_ratings', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

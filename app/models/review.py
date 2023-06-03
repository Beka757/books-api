from django.contrib.auth import get_user_model
from django.db import models
from .book import Book
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='user_reviews', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='book_reviews', on_delete=models.CASCADE)
    text = models.TextField(max_length=2000, verbose_name='Отзыв')
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True)

    def __str__(self):
        return self.text

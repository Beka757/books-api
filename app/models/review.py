from django.contrib.auth import get_user_model
from django.db import models
from .book import Book
from .rating import Rating


class Review(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='user_reviews', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='book_reviews', on_delete=models.CASCADE)
    text = models.TextField(max_length=2000, verbose_name='Отзыв')
    rating = models.ForeignKey(Rating, related_name='review_ratings', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.text

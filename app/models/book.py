from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=500, verbose_name='Описание')
    publication_date = models.DateField(verbose_name='Дата публикации')
    genres = models.ForeignKey('app.genre', on_delete=models.PROTECT, related_name='genre_books', verbose_name='Жанры')

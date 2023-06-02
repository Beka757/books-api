from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name='Жанр')

    def __str__(self):
        return self.name

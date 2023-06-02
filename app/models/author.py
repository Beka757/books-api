from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name='Автор')

    def __str__(self):
        return self.name

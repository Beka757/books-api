from django.contrib import admin
from app.models.book import Book
from app.models.author import Author
from app.models.genre import Genre
from app.models.review import Review
from app.models.favorite import Favorite


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(Favorite)

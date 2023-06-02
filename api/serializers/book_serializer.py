from rest_framework import serializers
from app.models.book import Book
from api.serializers.author_serializer import AuthorsSerializer
from api.serializers.genre_serializer import GenresSerializer


class BooksSerializer(serializers.ModelSerializer):
    author = AuthorsSerializer()
    genres = GenresSerializer()
    average_rating = serializers.SerializerMethodField()

    def get_average_rating(self, obj):
        return obj.average_rating()

    class Meta:
        model = Book
        exclude = ['description', 'publication_date']

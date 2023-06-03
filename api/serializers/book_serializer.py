from rest_framework import serializers
from app.models.book import Book
from api.serializers.author_serializer import AuthorsSerializer
from api.serializers.genre_serializer import GenresSerializer
from django_filters import rest_framework as filters


class BooksSerializer(serializers.ModelSerializer):
    author = AuthorsSerializer()
    genres = GenresSerializer()
    average_rating = serializers.SerializerMethodField()

    def get_average_rating(self, obj):
        return obj.average_rating()

    class Meta:
        model = Book
        exclude = ['description', 'publication_date']


class BookFilter(filters.FilterSet):
    min_publication_date = filters.DateFilter(field_name='publication_date', lookup_expr='gte')
    max_publication_date = filters.DateFilter(field_name='publication_date', lookup_expr='lte')

    class Meta:
        model = Book
        fields = ['genres', 'author', 'min_publication_date', 'max_publication_date']

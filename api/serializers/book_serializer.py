from rest_framework import serializers
from app.models.book import Book
from api.serializers.author_serializer import AuthorsSerializer
from api.serializers.genre_serializer import GenresSerializer
from api.serializers.review_serializer import ReviewSerializer
from django_filters import rest_framework as filters


class BooksSerializer(serializers.ModelSerializer):
    author = AuthorsSerializer()
    genre = GenresSerializer()
    average_rating = serializers.SerializerMethodField()
    detail_url = serializers.HyperlinkedIdentityField(view_name='book-detail', lookup_field='id')
    is_favorite = serializers.SerializerMethodField()

    def get_average_rating(self, obj):
        return obj.average_rating()

    def get_is_favorite(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return obj.book_favorites.filter(user=user).exists()
        return False

    class Meta:
        model = Book
        exclude = ['description', 'publication_date']


class BookFilter(filters.FilterSet):
    min_publication_date = filters.DateFilter(field_name='publication_date', lookup_expr='gte')
    max_publication_date = filters.DateFilter(field_name='publication_date', lookup_expr='lte')

    class Meta:
        model = Book
        fields = ['genre', 'author', 'min_publication_date', 'max_publication_date']


class BookDetailSerializer(serializers.ModelSerializer):
    author = AuthorsSerializer()
    genre = GenresSerializer()
    average_rating = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True, read_only=True, source='get_reviews')

    def get_average_rating(self, obj):
        return obj.average_rating()

    class Meta:
        model = Book
        fields = '__all__'

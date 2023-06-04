from rest_framework import serializers
from app.models.review import Review
from api.serializers.user_serializer import UserSerializer


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Review
        fields = ['user', 'rating', 'text']


class ReviewCreateSerializer(serializers.ModelSerializer):
    book = serializers.IntegerField(write_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Review
        fields = ['book', 'user', 'text', 'rating']

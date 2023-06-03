from rest_framework import serializers
from app.models.review import Review
from api.serializers.user_serializer import UserSerializer


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    rating = serializers.SerializerMethodField()

    def get_rating(self, review):
        if review.rating:
            return review.rating.rating
        return None

    class Meta:
        model = Review
        fields = ['user', 'rating', 'text']

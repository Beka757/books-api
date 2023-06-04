from rest_framework import serializers
from app.models.favorite import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    book = serializers.IntegerField(write_only=True)

    class Meta:
        model = Favorite
        fields = '__all__'

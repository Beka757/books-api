from rest_framework import serializers
from app.models.genre import Genre


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']

from rest_framework import serializers
from app.models.author import Author


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']

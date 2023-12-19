from rest_framework import serializers
from authors.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.username")

    class Meta:
        model = Author
        fields = ["id", "name", "book_count", "books_authored", "created_by"]

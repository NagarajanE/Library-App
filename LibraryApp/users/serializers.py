from rest_framework import serializers
from django.contrib.auth.models import User
from authors.models import Author

class UserSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(many=False,queryset=Author.objects.all())
    
    class Meta:
        model = User
        fields = ['id', 'username', 'author']
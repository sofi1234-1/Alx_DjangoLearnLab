from rest_framework import serializers
from .models import Author, Book
from datetime import date

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()  # Nested serializer

    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value 
   
   # ... code ...
class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book model instances, including nested author information.
    """
       # ... code ...
   

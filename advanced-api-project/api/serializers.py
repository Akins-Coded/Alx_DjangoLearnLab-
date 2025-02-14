from rest_framework import serializers
from .models import Book, Author
from datetime import date



class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        Field =  ['id', 'title', 'author', 'publication_year']

    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("The publication year cannot be in the future.")
        return value    

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = "__all__"

       
from rest_framework.serializers import ModelSerializer
from mytig.models import Book

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'language', 'releaseDate')

class BookContentSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'language', 'releaseDate', 'content')
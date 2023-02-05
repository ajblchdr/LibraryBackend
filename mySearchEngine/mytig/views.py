import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from mytig.config import baseUrl
from mytig.config import randomImageUrl
from mytig.models import Book
from mytig.serializers import BookSerializer, BookContentSerializer
from mytig.kmp import KMP
import re

class BookViewSet(APIView):
    def get(self, request, format=None):
        res=[]
        for book in Book.objects.all():
            serializer = BookSerializer(book)
            res.append(serializer.data)
        return Response(res)

class BookDetailViewSet(APIView):
    def get (self, request, pk, format=None):
        book = Book.objects.get(pk=pk)
        serializer = BookContentSerializer(book)
        return Response(serializer.data)

class BookSearchKMP(APIView):
    def get(self, request, txt, format=None):
        res = []
        books = Book.objects.all()
        for book in books:
            kmp = KMP()
            kmp.KMPSearch(txt,book.content)
            if kmp.isKmp is True:
                serializer = BookSerializer(book)
                res.append(serializer.data)
        return Response(res)

class BookSearchRegex(APIView):
    def get (self, request, txt, format=None):
        res = []
        books = Book.objects.all()
        for book in books:
            lines=re.split('\n', book.content)
            for line in lines :
                if re.compile(txt).search(line):
                    serializer = BookSerializer(book)
                    res.append(serializer.data)
                    break
        return Response(res)

class BookFilterByLanguage(APIView):
    def get (self, request, lang, format=None):
        res = []
        books = Book.objects.all()
        for book in books:
            if lang in book.language:
                serializer = BookSerializer(book)
                res.append(serializer.data)
        return Response(res)
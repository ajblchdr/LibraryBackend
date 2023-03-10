import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from mytig.config import baseUrl
from mytig.config import randomImageUrl
from mytig.models import Book
from mytig.serializers import BookSerializer, BookContentSerializer

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

"""
# Create your views here.
class RedirectionListeDeProduits(APIView):
    def get(self, request, format=None):
        response = requests.get(baseUrl+'products/')
        jsondata = response.json()
        return Response(jsondata)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"

class RedirectionDetailProduit(APIView):
    def get(self, request, pk, format=None):
        try:
            response = requests.get(baseUrl+'product/'+str(pk)+'/')
            jsondata = response.json()
            return Response(jsondata)
        except:
            raise Http404
#    def put(self, request, pk, format=None):
#        NO DEFITION of put --> server will return "405 NOT ALLOWED"
#    def delete(self, request, pk, format=None):
#        NO DEFITION of delete --> server will return "405 NOT ALLOWED"

###########################
#...TME8 part II starts...#
from rest_framework import renderers
from django.http import Http404

class JPEGRenderer(renderers.BaseRenderer):
    media_type = 'image/jpeg'
    format = 'jpg'
    charset = None
    render_style = 'binary'

    def render(self, data, media_type=None, renderer_context=None):
        return data

#Uncomment if images may iclude PNG
#class PNGRenderer(renderers.BaseRenderer):
#    media_type = 'image/png'
#    format = 'png'
#    charset = None
#    render_style = 'binary'
#
#    def render(self, data, media_type=None, renderer_context=None):
#        return data

import secrets

class ProduitImageRandom(APIView):
    renderer_classes = [JPEGRenderer]
#Uncomment if images may iclude PNG
#    renderer_classes = [JPEGRenderer,PNGRenderer]
    def get(self, request, pk, format=None):
        try:
            response = requests.get(secrets.choice(randomImageUrl))
            return Response(response)
        except:
            raise Http404

class ProduitImage(APIView):
    renderer_classes = [JPEGRenderer,renderers.JSONRenderer]
#Uncomment if images may iclude PNG
#    renderer_classes = [JPEGRenderer,PNGRenderer]
    def get(self, request, pk, image_id, format=None):
        if image_id<0 or image_id>len(randomImageUrl):
            return Response({'detail': 'Not found.'}, content_type='application/json')
        try:
            response = requests.get(randomImageUrl[image_id])
            return Response(response)
        except:
            raise Http404

#...end of TME8 part II...#
###########################

from mytig.models import ProduitEnPromotion
from mytig.serializers import ProduitEnPromotionSerializer

class PromoList(APIView):
    def get(self, request, format=None):
        res=[]
        for prod in ProduitEnPromotion.objects.all():
            serializer = ProduitEnPromotionSerializer(prod)
            response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
            jsondata = response.json()
            res.append(jsondata)
        return Response(res)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"

class PromoDetail(APIView):
    def get_object(self, pk):
        try:
            return ProduitEnPromotion.objects.get(pk=pk)
        except ProduitEnPromotion.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        prod = self.get_object(pk)
        serializer = ProduitEnPromotionSerializer(prod)
        response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
        jsondata = response.json()
        return Response(jsondata)
#    def put(self, request, pk, format=None):
#        NO DEFITION of put --> server will return "405 NOT ALLOWED"
#    def delete(self, request, pk, format=None):
#        NO DEFITION of delete --> server will return "405 NOT ALLOWED"
"""

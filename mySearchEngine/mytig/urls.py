from django.urls import path
from mytig import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('books/', views.BookViewSet.as_view()),
    path('book/<int:pk>', views.BookDetailViewSet.as_view())
]

"""
    path('products/', views.RedirectionListeDeProduits.as_view()),
    path('product/<int:pk>/', views.RedirectionDetailProduit.as_view()),
###########################
#...TME8 part II starts...#
    path('product/<int:pk>/image/', views.ProduitImageRandom.as_view()),
    path('product/<int:pk>/image/<int:image_id>/', views.ProduitImage.as_view()),
#...end of TME8 part II...#
###########################
    path('onsaleproducts/', views.PromoList.as_view()),
    path('onsaleproduct/<int:pk>/', views.PromoDetail.as_view()),
"""

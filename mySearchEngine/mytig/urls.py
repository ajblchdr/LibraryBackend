from django.urls import path
from mytig import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('books/', views.BookViewSet.as_view()),
    path('book/<int:pk>', views.BookDetailViewSet.as_view()),
    path('books/kmp/<str:txt>', views.BookSearchKMP.as_view()),
    path('book/regex/<str:txt>', views.BookSearchRegex.as_view())
]

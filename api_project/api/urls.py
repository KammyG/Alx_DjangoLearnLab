from django.urls import path
from .views import BookList
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('books/', BookList.as_view(), name='book-list'),
]
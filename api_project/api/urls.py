from django.urls import path, include
from .views import BookList, BookViewSet
from .views import home
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('', home, name='home'),
    path('books/', BookList.as_view(), name='book-list'),
     path('', include(router.urls)), 
]
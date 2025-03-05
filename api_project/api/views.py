from django.http import JsonResponse
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework.viewsets import ModelViewSet


def home(request):
    return JsonResponse({"message": "Welcome to the API!"})

class BookList(ListAPIView): 
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
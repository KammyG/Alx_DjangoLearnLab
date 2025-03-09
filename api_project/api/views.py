from django.http import JsonResponse
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadOnly
from rest_framework import generics

def home(request):
    return JsonResponse({"message": "Welcome to the API!"})

class BookList(generics.ListAPIView): 
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] 
    permission_classes = [IsAdminOrReadOnly] 
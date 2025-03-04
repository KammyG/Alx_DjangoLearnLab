from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to the API!"})

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

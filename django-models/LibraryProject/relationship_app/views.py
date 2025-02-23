from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library


def home(request):
    return render(request, 'relationship_app/home.html')


# Function-Based View to List All Books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View for Library Details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

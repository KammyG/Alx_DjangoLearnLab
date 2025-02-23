from .models import Library
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library
from django.contrib.auth import login, logout
from django.contrib.auth.forms import  UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django import forms


def home(request):
    return render(request, 'relationship_app/home.html')
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")  # Redirect to book list or home page
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

# Custom Login View
class CustomLoginView(LoginView):
    template_name = "relationship_app/login.html"

# Custom Logout View
class CustomLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"

# Function-Based View to List All Books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View for Library Details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

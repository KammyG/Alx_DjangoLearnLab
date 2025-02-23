from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Book, Library
from django import forms


# Home View
def home(request):
    return render(request, "relationship_app/home.html")

# Register View
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect("home")  # Redirect to home or another page
    else:
        form = UserCreationForm()
    
    return render(request, "relationship_app/register.html", {"form": form})  # FIXED TEMPLATE PATH

# Login View
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    
    return render(request, "relationship_app/login.html", {"form": form})  # FIXED TEMPLATE PATH

# Logout View
def user_logout(request):
    logout(request)
    return redirect("login")  # Redirect to login page after logout

# Class-Based Login View
class CustomLoginView(LoginView):
    template_name = "relationship_app/login.html"

# Class-Based Logout View
class CustomLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"

# Function-Based View to List All Books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-Based View for Library Details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

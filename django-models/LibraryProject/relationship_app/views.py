from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import user_passes_test
from .models import Book, Library, UserProfile

# ============================
# Role-Based Access Control
# ============================

def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == "Admin"

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == "Librarian"

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == "Member"

# Admin View
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

# Librarian View
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

# Member View
@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")


# ============================
# Authentication Views
# ============================

def home(request):
    return render(request, "relationship_app/home.html")

# User Registration
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user, role="Member")  # Default role is Member
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    
    return render(request, "relationship_app/register.html", {"form": form})

# User Login
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    
    return render(request, "relationship_app/login.html", {"form": form})

# User Logout
def user_logout(request):
    logout(request)
    return redirect("login")

# Class-Based Login View
class CustomLoginView(LoginView):
    template_name = "relationship_app/login.html"

# Class-Based Logout View
class CustomLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"


# ============================
# Book and Library Views
# ============================

# List Books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Library Details (Class-Based View)
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

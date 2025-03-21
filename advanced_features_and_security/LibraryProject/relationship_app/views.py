from django.contrib.auth.decorators import permission_required  
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book, UserProfile
from .forms import BookForm
from .models import Library
from django.http import HttpResponse

# ============================
# Role-Based Access Control
# ============================
def some_view_function(request):
    return HttpResponse("Hello, this is a test view!")

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
# Book Management Views (Access Controlled)
# ============================

# List Books (Public)
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Add Book (Only Users with "can_add_book" Permission)
@permission_required("relationship_app.can_add_book", raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.created_by = request.user  # Track who added the book
            book.save()
            return redirect("list_books")
    else:
        form = BookForm()
    return render(request, "relationship_app/add_book.html", {"form": form})

# Edit Book (Only Users with "can_change_book" Permission)
@permission_required("relationship_app.can_change_book", raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("list_books")
    else:
        form = BookForm(instance=book)
    return render(request, "relationship_app/edit_book.html", {"form": form, "book": book})

# Delete Book (Only Users with "can_delete_book" Permission)
@permission_required("relationship_app.can_delete_book", raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("list_books")
    return render(request, "relationship_app/delete_book.html", {"book": book})


# ============================
# Library Detail View
# ============================

# Library Details (Class-Based View)
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

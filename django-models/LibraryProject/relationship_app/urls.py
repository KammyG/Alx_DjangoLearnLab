from django.urls import path
from .views import list_books
from .views import views 
from .views import (
    home, register, user_login, user_logout, add_book, edit_book, delete_book,
    admin_view, librarian_view, member_view, LibraryDetailView
)
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Authentication
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name="relationship_app/login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="relationship_app/logout.html"), name='logout'),


    # Role-Based Views
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),

    # Book Management
    path('books/', list_books, name='list_books'),
    path('add_book/', add_book, name='add_book'),  
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),  
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),  

    # Library Details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]

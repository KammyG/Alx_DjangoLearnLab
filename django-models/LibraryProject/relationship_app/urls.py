from django.urls import path
from . import views

urlpatterns = [
    # Authentication URLs (Choose Either CustomLoginView or user_login)
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),  # Using function-based login
    path("logout/", views.user_logout, name="logout"),

    # Homepage
    path("", views.home, name="home"),

    # Books List
    path("books/", views.list_books, name="list_books"),

    # Library Detail View
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
]

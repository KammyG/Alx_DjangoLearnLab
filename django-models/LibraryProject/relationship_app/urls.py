from django.urls import path
from . import views
from .views import list_books, LibraryDetailView
from .views import register, CustomLoginView, CustomLogoutView

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    
    path('', views.home, name='home'),  # Homepage URL
    path('books/', views.list_books, name='list_books'),

    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]


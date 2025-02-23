from django.urls import path
from . import views
from .views import list_books, LibraryDetailView

urlpatterns = [
    
    path('', views.home, name='home'),  # Homepage URL
    path('books/', views.list_books, name='list_books'),

    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]


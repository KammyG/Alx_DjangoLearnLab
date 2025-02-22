import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    author = Author.objects.filter(name=author_name).first()
    if author:
        books = Book.objects.filter(author=author)
        return [book.title for book in books]
    return []

def get_books_in_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if library:
        return [book.title for book in library.books.all()]
    return []

def get_librarian_for_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if library:
        librarian = Librarian.objects.filter(library=library).first()
        return librarian.name if librarian else "No librarian assigned"
    return "Library not found"

if __name__ == "__main__":
    print("Books by 'J.K. Rowling':", get_books_by_author("J.K. Rowling"))
    print("Books in 'City Library':", get_books_in_library("City Library"))
    print("Librarian of 'City Library':", get_librarian_for_library("City Library"))

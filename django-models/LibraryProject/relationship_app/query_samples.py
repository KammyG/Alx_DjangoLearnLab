import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)  # Use .get() instead of .filter().first()
        books = Book.objects.filter(author=author)
        return [book.title for book in books]
    except Author.DoesNotExist:
        return []


def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)  # Using get() instead of filter().first()
        return [book.title for book in library.books.all()]
    except Library.DoesNotExist:
        return "Library not found"



def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian.name
    except Library.DoesNotExist:
        return "Library not found"
    except Librarian.DoesNotExist:
        return "No librarian assigned"


if __name__ == "__main__":
    print("Books by 'J.K. Rowling':", get_books_by_author("J.K. Rowling"))
    print("Books in 'City Library':", get_books_in_library("City Library"))
    print("Librarian of 'City Library':", get_librarian_for_library("City Library"))

from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        """ Set up test user and initial book data """
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.book1 = Book.objects.create(title="Book One", author="Author A", publication_year=2000)
        self.book2 = Book.objects.create(title="Book Two", author="Author B", publication_year=2005)
        self.book3 = Book.objects.create(title="Book Three", author="Author C", publication_year=2010)

        self.client.login(username='testuser', password='testpass')  # Authenticate user

    # ✅ Test retrieving the book list
    def test_get_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    # ✅ Test creating a new book
    def test_create_book(self):
        data = {"title": "New Book", "author": "Author D", "publication_year": 2022}
        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)

    # ✅ Test retrieving a specific book
    def test_get_book_detail(self):
        response = self.client.get(f'/api/books/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Book One")

    # ✅ Test updating a book
    def test_update_book(self):
        data = {"title": "Updated Book", "author": "Author A", "publication_year": 2001}
        response = self.client.put(f'/api/books/update/{self.book1.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    # ✅ Test deleting a book
    def test_delete_book(self):
        response = self.client.delete(f'/api/books/delete/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)

    # ✅ Test filtering books by title
    def test_filter_books(self):
        response = self.client.get('/api/books/?title=Book One')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Book One")

    # ✅ Test searching books by author
    def test_search_books(self):
        response = self.client.get('/api/books/?search=Author B')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], "Author B")

    # ✅ Test ordering books by publication year
    def test_order_books(self):
        response = self.client.get('/api/books/?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2000)  # Oldest book first

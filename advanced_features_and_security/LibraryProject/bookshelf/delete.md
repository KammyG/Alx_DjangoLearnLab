# Delete the Book Instance

```python
from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print(Book.objects.all())  # This should return an empty queryset if successful

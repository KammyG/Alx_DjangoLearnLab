from django.db import models

class Author(models.Model):
    """Model representing an author."""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """Model representing a book with an author relationship."""
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, unique=True, null=True, blank=True)
    pages = models.IntegerField(default=100)
    cover_image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

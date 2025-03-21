from django import forms
from .models import Book
from .models import ExampleModel

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
class ExampleForm(forms.ModelForm):
    class Meta:
        model = ExampleModel  # Replace with your actual model
        fields = '__all__' 
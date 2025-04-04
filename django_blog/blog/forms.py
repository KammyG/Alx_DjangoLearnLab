from django import forms
from .models import Post
from .models import Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "tags"]

        class CommentForm(forms.ModelForm):
          class Meta:
           model = Comment
           fields = ['content']
           widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
from django.forms import ModelForm
# from django import forms
from .models import Post,User, Comment
from django.contrib.auth.forms import UserCreationForm

class PostForm(ModelForm):
    
    class Meta:
        model = Post
        fields = '__all__'

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        # exclude = []

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'avatar', 'bio', 'email', 'username']

    

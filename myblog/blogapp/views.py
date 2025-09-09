from django.shortcuts import render
from .models import Category, Comment, Post, Profile
# Create your views here.
def home(request):
    posts = Post.objects.all()
    context ={
        'posts': posts
    }
    return render(request, 'blogapp/home.html', context)
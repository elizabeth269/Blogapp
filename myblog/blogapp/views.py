from django.shortcuts import render, redirect
from .models import Category, Comment, Post, Profile
from .forms import PostForm 
from django.contrib import messages


# Create your views here.
def home(request):
    posts = Post.objects.all()
    context ={
        'posts': posts
    }
    return render(request, 'blogapp/home.html', context)


def post(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'posts': post
    }
    return render(request, 'blogapp/post.html', context)


def createPost(request):

    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog post has been created successfully")
            return redirect('/')
        
    else:
        form = PostForm()
        messages.error(request, 'an error occured')
      
        
    return render(request, 'createPost.html')
        

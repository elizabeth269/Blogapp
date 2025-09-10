from django.shortcuts import render, redirect
from .models import Category, Comment, Post
from .forms import PostForm 
from django.contrib import messages
from django.db.models import Q


# Create your views here.

def loginPage(request):
    pass

def logoutPage(Request):
    pass

def registration(request):
    pass

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    posts = Post.objects.filter(
        Q(title__icontains=q) |
        Q(category__name__icontains=q) |
        Q(description__icontains=q)
    )
    posts_count = posts.count()
    

    context ={
        'posts': posts,
        'posts_count': posts_count,

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
            return redirect('home')
        else: 
            messages.error(request, 'an error occured')
    else:
        form = PostForm()
        
    context = {
        'form': form
    }
        
    return render(request, 'blogapp/createPost.html', context)
    

def editPost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, f'you have edited {post.title} successfully')
            return redirect('home')
        
    context = {
        'form': form,
        'post': post
    }
    
    return render(request, 'blogapp/editPost.html', context)

    
def deletePost(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        post.delete()
        messages.success(request, f'you have deleted {post.title} successfully')
        return redirect('home')
    
    return render(request, 'blogapp/deletePost.html',{'obj': post})
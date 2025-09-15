from django.shortcuts import render, redirect
from .models import Category, Comment, Post, User
from .forms import PostForm, MyUserCreationForm,CommentForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



# Create your views here.

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)

        except:
            messages.error(request, 'user does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            messages.error(request, 'Username OR password does not exit')

    context = {'page': page}
    return render(request, 'blogapp/login-register.html', context)

def logoutPage(request):
    logout(request)
    return redirect('home')


def registration(request):
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) # create the user but don't save it yet because i might want to modify the user object before saving it in the database
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Registration successful.')
            return redirect('login')
        else:
            messages.error(request, 'registration is unsuccessful')

    else:
        form = MyUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'blogapp/login-register.html', context)

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    posts = Post.objects.filter(
        Q(title__icontains=q) |
        Q(category__name__icontains=q) |
        Q(description__icontains=q)
    )
    posts_count = posts.count()
    # messages.error(request, 'an error occured')

    context ={
        'posts': posts,
        'posts_count': posts_count,

    }
    return render(request, 'blogapp/home.html', context)


def post(request, pk):
    post = Post.objects.get(id=pk)
    post_comments = post.post_comments.all()

    if request.method == 'POST':
        body=request.POST.get('body')
        # parent_id=request.POST.get('parent_id')
        if body:
            comment = Comment.objects.create(
                author=request.user, post=post,body=body,
                # parent_id=parent_id if parent_id else None,
            )
        return redirect('post', pk=post.id)
    context = {
        'post': post,
        'post_comments': post_comments
    }
    return render(request, 'blogapp/post.html', context)

def reply_comment(request):
    pass


def userProfile(request,pk):
    author = User.objects.get(id=pk)
    posts = author.posts.all()
    comment = author.comment_set.all()
    comment_count = comment.count()
    categories = Category.objects.all()
    context = {
        'author': author,
        'comment': comment,
        'posts': posts,
        'categories': categories,
        'comment_count':comment_count
    }
    return render(request, 'blogapp/profile.html', context)

def commentFeed(request):
    comments = Comment.objects.all()
    context = {
        'comments': comments,
    }
    return render(request, 'blogapp/comment_feed.html', {'comments': comments})

@login_required(login_url='login')
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
    
@login_required(login_url='login')
def editPost(request, pk):
    post = Post.objects.get(id=pk)
    if request.user != post.author:
        return HttpResponse("You are not allowed to edit this post.")

    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, f'you have edited {post.title} successfully')
            return redirect('post', pk=post.id)
        
    context = {
        'form': form,
        'post': post
    }
    
    return render(request, 'blogapp/editPost.html', context)

@login_required(login_url='login')   
def deletePost(request, pk):
    post = Post.objects.get(id=pk)
    if request.user != post.author:
        return HttpResponse("You are not allowed to delete this post.")

    if request.method == "POST":
        post.delete()
        messages.success(request, f'you have deleted {post.title} successfully')
        return redirect('home')
    
    return render(request, 'blogapp/deletePost.html',{'obj': post})




@login_required(login_url='login')
def deleteComment(request, pk):
    comment = Comment.objects.get(id=pk)
    post = comment.post

    if request.user != comment.author:
        return HttpResponse("You are not allowed to delete this comment.")

    if request.method == 'POST':
        comment.delete()
        return redirect('post', pk=post.id)
    return render(request, 'blogapp/deleteComment.html', {'obj': comment})

@login_required(login_url='login')
def editComment(request, pk):
    comment = Comment.objects.get(id=pk)
    if request.user != comment.author:
        return HttpResponse("You are not allowed to edit this comment.")

    form = CommentForm(instance=comment)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, f'you have edited {comment.body} successfully')
            return redirect('post',pk=comment.post.id)
        
    context = {
        'form': form,
        'comment': comment
    }
    
    return render(request, 'blogapp/editComment.html', context)

def like_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.user in comment.likes.all():
        comment.likes.remove(request.user)

    else:
        comment.likes.add(request.user)
    return redirect('post', pk=comment.post.id)





    # if request.user != post.author and not request.user.is_staff and not request.user.is_superuser:
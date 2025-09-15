from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']



class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    description = models.CharField(max_length=300, blank=False)
    image = models.ImageField(upload_to='posts/', blank=True, null=True)  
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    published = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-updated_at', '-created_at']
        
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # parent = models.ForeignKey(
    #     'self', null=True, blank=True, related_name="replies", on_delete=models.CASCADE
    # )
    likes = models.ManyToManyField(User, related_name="comment_likes", blank=True)

    @property
    def like_count(self):
        return self.likes.count()

    @property
    def is_reply(self):
        return self.parent is not None


    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'


# class Profile(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
#     bio = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.user.username
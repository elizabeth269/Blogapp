from django.contrib import admin
from .models import Category, Post, User, Comment
# Register your models here.
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
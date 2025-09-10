from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<str:pk>/', views.post, name='post'),
    path('creatPost', views.createPost, name='create'),
    path('editPost/<str:pk>/', views.editPost, name='edit')
]
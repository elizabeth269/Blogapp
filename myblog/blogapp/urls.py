from django.urls import path
from . import views

urlpatterns = [
    path('loginPage', views.loginPage,name='login'),
    path('logoutPage', views.logoutPage,name='logout'),
    path('registration', views.registration,name='register'),
    path('', views.home, name='home'),
    path('post/<str:pk>/', views.post, name='post'),
    path('creatPost', views.createPost, name='create'),
    path('editPost/<str:pk>/', views.editPost, name='edit'),
    path('deletePost/<str:pk>/', views.deletePost, name='delete'),
    path('editComment/<str:pk>/', views.editComment, name='edit-comment'),
    path('deleteComment/<str:pk>/', views.deleteComment, name='delete'),
]
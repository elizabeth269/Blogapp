from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('loginPage', views.loginPage,name='login'),
    path('logoutPage', views.logoutPage,name='logout'),
    path('registration', views.registration,name='register'),
    path('', views.home, name='home'),
    path('post/<str:pk>/', views.post, name='post'),
    path('profile/<str:pk>/', views.userProfile, name='profile'),
    path('updateUser/<str:pk>/', views.updateUser, name='update-user'),
    path('deleteUser/<str:pk>/', views.deleteUser, name='delete-user'),
    path('creatPost', views.createPost, name='create'),
    path('editPost/<str:pk>/', views.editPost, name='edit'),
    path('deletePost/<str:pk>/', views.deletePost, name='delete'),
    path('editComment/<str:pk>/', views.editComment, name='edit-comment'),
    path('deleteComment/<str:pk>/', views.deleteComment, name='delete'),
    path('comment/<str:comment_id>/like/', views.like_comment, name='like_comment'),
     path("comment-feed/", views.commentFeed, name="comment_feed"),
    path('post/<str:pk>/reply/<str:parent_id>/', views.reply_comment, name='reply_comment'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
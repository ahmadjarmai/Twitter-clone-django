from django.urls import path,include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('tweet/create/', views.create_tweet, name='create_tweet'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('edit/', views.edit, name ='edit'),
    path('like/<int:pk>/', views.tweet_like, name='like'),
    path('<int:pk>/retweet', views.retweet, name ='retweet'),
    path('<int:tweet_id>/comment', views.tweet_comment, name="comment"),
    path('follow/<int:user_id>/', views.follow, name='follow'),
    path('unfollow/<int:user_id>/', views.unfollow, name='unfollow'),
    path('activity/', views.activity_stream, name='activity'),
]

if settings.DEBUG:
 urlpatterns += static(settings.MEDIA_URL,
 document_root=settings.MEDIA_ROOT)
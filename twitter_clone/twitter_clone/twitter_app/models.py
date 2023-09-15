from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class Tweet(models.Model):
    content = models.CharField(max_length=280)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='tweet_liked',blank=True)
    retweet_from =models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    retweet_count =models.PositiveIntegerField(default=0)
    
    def __str___(self) :
      return f"{self.author.username}"
      
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.CharField(max_length=160)
    location = models.CharField(max_length=30, blank=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',null=True, blank=True)
    
    def __str__(self):
      return f'Profile of {self.user.username}'

class Comment(models.Model):
   tweet = models.ForeignKey(Tweet,on_delete=models.CASCADE,related_name='comments')
   body = models.TextField()
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)
   active = models.BooleanField(default=True)
 
   class Meta:
       ordering = ['created']
       indexes = [
       models.Index(fields=['created']),
     ]
   def __str__(self):
    return f'Comment by {request.user} on {self.tweet}'
    
    
class Contact(models.Model):
   user_from = models.ForeignKey('auth.User', related_name='rel_from_set', on_delete=models.CASCADE)
   user_to = models.ForeignKey('auth.User',related_name='rel_to_set',on_delete=models.CASCADE)
   created = models.DateTimeField(auto_now_add=True)
   
   class Meta:
     indexes = [
            models.Index(fields=['-created']),
     ]
     ordering = ['-created']
 
   def __str__(self):
        return f'{self.user_from} follows {self.user_to}'

class Follow(models.Model):
    user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    followed_user = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'followed_user')


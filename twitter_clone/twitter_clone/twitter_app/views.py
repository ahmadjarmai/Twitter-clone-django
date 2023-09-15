from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import Tweet, Profile,Contact,Follow
from django.contrib.auth.decorators import login_required 
from .forms import UserRegistrationForm,UserEditForm, ProfileEditForm,CommentForm
from actions.utils import create_action
from actions.models import Activity 

from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_POST


@login_required
def home(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'twitter_clone/home.html', {'tweets': tweets})

def register(request):
  if request.method == 'POST':
    user_form = UserRegistrationForm(request.POST)
    if user_form.is_valid():
      new_user = user_form.save(commit=False)
      new_user.set_password(user_form.cleaned_data['password'])
      new_user.save()
      Profile.objects.create(user=new_user)
      return render(request,'twitter_clone/register_done.html', {'new_user': new_user})
  else:
    user_form = UserRegistrationForm()
  return render(request,'twitter_clone/register.html',{'user_form': user_form})

@login_required
def edit(request):
  if request.method == 'POST':
    user_form = UserEditForm(instance=request.user,data=request.POST)
    profile_form = ProfileEditForm(
    instance=request.user.profile,data=request.POST, files=request.FILES)
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
  else:
    user_form = UserEditForm(instance=request.user)
    profile_form = ProfileEditForm(instance=request.user.profile)
  return render(request,'twitter_clone/edit.html',{'user_form': user_form, 'profile_form': profile_form})


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    tweets = Tweet.objects.all()
    #following = Follower.objects.filter(user=user).count()
    #followers = Follower.objects.filter(following=user).count()
    return render(request, 'twitter_clone/profile.html', {'user': user,'tweets': tweets})

@login_required
def create_tweet(request, retweet=None):
    if request.method == 'POST':
        content = request.POST.get('content')
        tweet = Tweet(content=content, author=request.user)
        tweet.save()
        create_action(request.user, 'New Tweet',tweet )
        return redirect('home')
    return render(request, 'twitter_clone/create_tweet.html')
    

@login_required
def tweet_like(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    user = request.user
    if user in tweet.users_like.all():
      tweet.users_like.remove(user)
      liked = False
    else:
        tweet.users_like.add(user)
        create_action(request.user, 'Likes', tweet)
        liked = True
    return redirect('home')

@login_required
def tweet_comment(request, tweet_id):
   tweet= get_object_or_404(Tweet, id=tweet_id)
   comment = None
 # A comment was posted
   if request.method =='POST' :
     form = CommentForm(data=request.POST)
     if form.is_valid():
       comment = form.save(commit=False)
       comment.tweet = tweet
       comment.author = request.user
       comment.save()
       create_action(request.user, 'Comment', comment)
       return redirect("home")
   else :
     form =CommentForm()
   return render(request, 'twitter_clone/comment.html',
 {'tweet': tweet,
 'form': form,
 'comment':comment })
 
@login_required
def retweet(request, pk):
    original_tweet = get_object_or_404(Tweet, pk=pk)
    new_tweet = Tweet(author=original_tweet.author, content=original_tweet.content, retweet_from=original_tweet)
    new_tweet.save()
    create_action(request.user, 'retweet', new_tweet)
    
    original_tweet.retweet_count +=1
    original_tweet.save()
    
    return redirect('home')
 
@login_required
def follow(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    if request.user != user_to_follow:
        Follow.objects.get_or_create(user=request.user, followed_user=user_to_follow)
        create_action(request.user, 'Follow', user_to_follow)
    return redirect('profile', username= user_to_follow.username)

@login_required
def unfollow(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)
    Follow.objects.filter(user=request.user, followed_user=user_to_unfollow).delete()
    return redirect('profile', username=user_to_unfollow.username)

@login_required
def activity_stream(request):
    following_ids = request.user.following.values_list('id', flat=True)
    activities = Activity.objects.exclude(user=request.user)
    
    if following_ids :
      activities=Activity.filter(user_id__in=following_ids)
    activities=activities[:10]
    return render(request, 'twitter_clone/activity_stream.html', {'activities': activities})
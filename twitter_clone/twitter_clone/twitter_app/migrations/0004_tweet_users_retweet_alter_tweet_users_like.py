# Generated by Django 4.2 on 2023-08-13 12:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('twitter_app', '0003_tweet_users_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='users_retweet',
            field=models.ManyToManyField(blank=True, related_name='tweet_retweet', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='users_like',
            field=models.ManyToManyField(blank=True, related_name='tweet_liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
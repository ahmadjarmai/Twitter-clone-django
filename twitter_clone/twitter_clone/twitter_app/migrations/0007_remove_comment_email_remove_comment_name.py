# Generated by Django 4.2 on 2023-08-15 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_app', '0006_rename_post_comment_tweet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
    ]

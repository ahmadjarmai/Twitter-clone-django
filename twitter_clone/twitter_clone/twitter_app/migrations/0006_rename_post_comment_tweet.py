# Generated by Django 4.2 on 2023-08-15 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_app', '0005_comment_comment_twitter_app_created_ffa211_idx'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='tweet',
        ),
    ]

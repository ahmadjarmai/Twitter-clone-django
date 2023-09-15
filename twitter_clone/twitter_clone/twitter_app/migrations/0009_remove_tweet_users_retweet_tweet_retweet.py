# Generated by Django 4.2 on 2023-08-15 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_app', '0008_contact_delete_follower_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='users_retweet',
        ),
        migrations.AddField(
            model_name='tweet',
            name='retweet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='twitter_app.tweet'),
        ),
    ]

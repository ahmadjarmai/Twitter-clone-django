# Generated by Django 4.2 on 2023-08-18 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0002_activity_delete_action'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterUniqueTogether(
            name='activity',
            unique_together=set(),
        ),
        migrations.AddIndex(
            model_name='activity',
            index=models.Index(fields=['-timestamp'], name='actions_act_timesta_67490d_idx'),
        ),
        migrations.AddIndex(
            model_name='activity',
            index=models.Index(fields=['content_type', 'object_id'], name='actions_act_content_46534d_idx'),
        ),
    ]
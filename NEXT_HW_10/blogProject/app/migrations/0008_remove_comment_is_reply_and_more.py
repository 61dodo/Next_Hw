# Generated by Django 5.0.4 on 2024-04-06 09:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_comment_is_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='is_reply',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='parent_comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.comment'),
        ),
    ]

# Generated by Django 2.0.13 on 2020-07-22 14:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Question',
        ),
    ]

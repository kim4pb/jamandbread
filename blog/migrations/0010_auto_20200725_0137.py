# Generated by Django 2.0.13 on 2020-07-24 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text_a',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='text_b',
            field=models.TextField(),
        ),
    ]

# Generated by Django 4.0 on 2021-12-11 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publication_year',
        ),
        migrations.RemoveField(
            model_name='book',
            name='rating',
        ),
    ]
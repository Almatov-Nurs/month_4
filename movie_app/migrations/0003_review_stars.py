# Generated by Django 4.0.2 on 2022-02-17 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_movie_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='stars',
            field=models.PositiveSmallIntegerField(max_length=5, null=True),
        ),
    ]
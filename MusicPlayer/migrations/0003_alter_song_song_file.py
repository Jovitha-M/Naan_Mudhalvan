# Generated by Django 4.1.7 on 2024-04-07 15:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("MusicPlayer", "0002_song_image_url_song_movie"),
    ]

    operations = [
        migrations.AlterField(
            model_name="song",
            name="song_file",
            field=models.FileField(upload_to="music"),
        ),
    ]

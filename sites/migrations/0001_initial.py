# Generated by Django 3.0.5 on 2023-07-06 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='YouTubeVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('video_id', models.CharField(max_length=20)),
                ('thumbnail_url', models.URLField()),
                ('search_query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.SearchQuery')),
            ],
        ),
        migrations.CreateModel(
            name='UdemyCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=10)),
                ('thumbnail', models.URLField()),
                ('link', models.URLField()),
                ('search_query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.SearchQuery')),
            ],
        ),
    ]

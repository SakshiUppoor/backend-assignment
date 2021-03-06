# Generated by Django 4.0 on 2021-12-19 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('channel_name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(max_length=255)),
                ('thumbnail_url', models.URLField(max_length=255)),
                ('published_at', models.DateTimeField()),
            ],
        ),
    ]

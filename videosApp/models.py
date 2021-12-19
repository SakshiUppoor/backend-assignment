from django.db import models

# Create your models here.

class Video(models.Model):
    id = models.CharField(max_length=20, primary_key=True)  # video ID of the vide eg: 8awhq8fsD-Q
    title = models.CharField(max_length=255, blank=True, null=True)
    channel_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=255)
    thumbnail_url = models.URLField(max_length=255)
    published_at = models.DateTimeField()
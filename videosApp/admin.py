from django.contrib import admin
from .models import Video
# Register your models here.

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "channel_name", "published_at")
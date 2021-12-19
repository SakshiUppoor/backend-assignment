from django.apps import AppConfig


class VideosConfig(AppConfig):
    name = 'videosApp'
    def ready(self):
        from .utils import video_fetcher
        video_fetcher.start()

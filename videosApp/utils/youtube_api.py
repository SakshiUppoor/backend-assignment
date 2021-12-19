from googleapiclient.discovery import build
from django.db import IntegrityError
from datetime import datetime, timedelta
from ..models import Video
import json

# Fetching youtube API Key
with open('./chessYoutube/credentials.json', 'r') as f:
    YOUTUBE_API_KEY = json.load(f)["YOUTUBE_API_KEY"]

# Building the youtube API service
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

def fetchLatestVideos():
    """
    Fetches and stores the latest 10 
    chess videos published an hour ago
    """
    
    # Timestamp of 1 hour before
    an_hour_ago = (datetime.utcnow() - timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%SZ")

    request = youtube.search().list(
        part='snippet',
        type='video',
        q='chess', # Get chess videos
        order='date', # Order in reverse chronological order
        maxResults=10, # Fetch max 10 videos at a time
        publishedAfter=an_hour_ago # Fetch videos posted not more than an hour ago
    )

    response = request.execute()
    videos = storeVideos(response["items"])
    return {"videos":videos}

def storeVideos(videos):
    saved_videos = []
    for video in videos:
        video_dict = {
            "id":video["id"]["videoId"],
            "title":video["snippet"]["title"],
            "description":video["snippet"]["description"],
            "thumbnail_url":video["snippet"]["thumbnails"]["default"]["url"],
            "channel_name":video["snippet"]["channelTitle"],
            "published_at":video["snippet"]["publishedAt"],
        }
        try:
            Video.objects.create(**video_dict)
            saved_videos.append(video_dict)
        except IntegrityError: 
            """
            If video with same id is already saved in db,
            then the same video got fetched again
            To avoid duplication, we don't want to save this.
            Hence, the Integrity exception is used
            """
            pass
    return saved_videos
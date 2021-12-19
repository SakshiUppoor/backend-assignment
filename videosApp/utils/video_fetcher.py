from apscheduler.schedulers.background import BackgroundScheduler
import atexit
from googleapiclient.discovery import build
from django.db import IntegrityError
from datetime import datetime, timedelta
from ..models import Video
import json

scheduler = BackgroundScheduler()

youtube, YOUTUBE_API_KEYS, i = (None, None, None)

def start():
    global youtube, YOUTUBE_API_KEYS, i
    print("Job added")
    # Fetching youtube API Key
    with open('./chessYoutube/credentials.json', 'r') as f:
        YOUTUBE_API_KEYS = json.load(f)["YOUTUBE_API_KEYS"]

    i=0
    # Building the youtube API service
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEYS[i])
    scheduler.add_job(fetchLatestVideos, 'interval', seconds=25)
    scheduler.start()
    atexit.register(terminate)
    
def terminate():
    print("Killing job")
    scheduler.shutdown()

def fetchLatestVideos():
    """
    Fetches the latest 10 chess 
    videos published an hour ago
    using the Yotube Data API
    and stores them in the database
    """
    global youtube, YOUTUBE_API_KEYS, i
    try:
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
        print(f"Fetched & saved {len(videos)}.")

    except Exception as e:
        if e.resp.status in [403, 429]:
            """
            If quota is exceeded, change API key
            to next available API key
            403 - Quota Exceeded
            429 - User rate limited
            """
            youtube.close()
            i += 1
            i = i%len(YOUTUBE_API_KEYS)
            print("Quota exceeded on current key...Using next available key")
            youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEYS[i])

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
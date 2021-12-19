from googleapiclient.discovery import build
from datetime import datetime, timedelta
import json

# Fetching youtube API Key
with open('./chessYoutube/credentials.json', 'r') as f:
    YOUTUBE_API_KEY = json.load(f)["YOUTUBE_API_KEY"]

# Building the youtube API service
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

def fetchLatestVideos():
    """
    Fetch the latest 10 chess videos published an hour ago
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
    return response
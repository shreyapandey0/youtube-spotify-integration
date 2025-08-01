# yt_scraper.py (Using YouTube API)
from googleapiclient.discovery import build
import pandas as pd
import os

# It's better to use environment variables for API keys
API_KEY = os.getenv("YOUTUBE_API_KEY", "AIzaSyC7h61TBD4_5AkmA4MaRaC4_bUg60o9cg8")  # ← Replace this or set env variable

def get_trending(api_key, region="IN", count=50):
    print(f"Fetching trending music videos for regions IN, US, GB (limit {count})...")
    youtube = build('youtube', 'v3', developerKey=api_key)
    total_results = []
    fetched = 0
    for region_code in ["IN", "US", "GB"]:
        request = youtube.videos().list(
            part='snippet,statistics,contentDetails',
            chart='mostPopular',
            regionCode=region_code,
            videoCategoryId='10',
            maxResults=50
        )
        response = request.execute()

        for item in response['items']:
            snippet = item['snippet']
            stats = item['statistics']
            content = item['contentDetails']
            total_results.append({
                "YouTube Title": snippet.get('title'),
                "Channel": snippet.get('channelTitle'),
                "Views": stats.get('viewCount', 'N/A'),
                "Likes": stats.get('likeCount', 'N/A'),
                "Comments": stats.get('commentCount', 'N/A'),
                "Upload Time": snippet.get('publishedAt'),
                "Duration": content.get('duration'),
                "Video URL": f"https://www.youtube.com/watch?v={item['id']}"
            })

        if len(total_results) >= count:
            break

    print(f"Fetched {len(total_results[:count])} videos in total.")
    return pd.DataFrame(total_results[:count])

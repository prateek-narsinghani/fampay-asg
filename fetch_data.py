from pprint import pprint
from apscheduler.schedulers.background import BackgroundScheduler
from config import Config

import googleapiclient.discovery
import googleapiclient.errors

next_token = None

def call_api(api_key, query, page_token=None):
    print("fetching", api_key, query, page_token)

    api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)
    
    try:
        request = youtube.search().list(
            part="snippet",
            maxResults=2,
            order="date",
            pageToken=page_token,
            q=query,
            relevanceLanguage="en",
            type="video"
        )
        response = request.execute()

        videos = []
        for search_result in response.get('items', []):
            # filter out only the videos
            if search_result['id']['kind'] == 'youtube#video':
                videos.append({
                    'title': search_result['snippet']['title'],
                    'description': search_result['snippet']['description'],
                    'video_id': search_result['id']['videoId'],
                    'thumbnail': search_result['snippet']['thumbnails']['default']['url'],
                    'published_at': search_result['snippet']['publishedAt'],
                    'channel_title': search_result['snippet']['channelTitle']

                })

        return videos, response.get('nextPageToken', None)
    except Exception as e:
        print('Error occurred:', e)
        return None, None


def fetch_youtube_videos():
    global next_token
    videos, next_token = call_api(Config.get_api_key(), Config.get_predefined_search_query(), next_token)
    pprint(videos)
    print(next_token)

sched = BackgroundScheduler(daemon=True)
sched.add_job(fetch_youtube_videos,'interval',seconds=5)
sched.start()
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


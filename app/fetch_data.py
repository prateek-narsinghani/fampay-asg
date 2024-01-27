from datetime import datetime, timedelta
from pprint import pprint
from apscheduler.schedulers.background import BackgroundScheduler
from app import app
from app.models import Video
from config import Config
from app import db

import googleapiclient.discovery
import googleapiclient.errors
import logging

logging.basicConfig(level=logging.INFO)
next_token = None


def call_api(api_key, query, page_token=None):
    print("fetching", api_key, query, page_token)

    api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(api_service_name,
                                              api_version,
                                              developerKey=api_key)

    try:
        published_after_time = datetime.utcnow() - timedelta(hours=1)
        published_after_str = published_after_time.strftime('%Y-%m-%dT%H:%M:%SZ')
        request = youtube.search().list(part="snippet",
                                        maxResults=2,
                                        order="date",
                                        pageToken=page_token,
                                        q=query,
                                        relevanceLanguage="en",
                                        type="video",
                                        publishedAfter=published_after_str)
        response = request.execute()

        videos = []
        for search_result in response.get('items', []):
            # filter out only the videos
            if search_result['id']['kind'] == 'youtube#video':
                published_at_str = search_result['snippet']['publishedAt']
                published_at = datetime.strptime(published_at_str, "%Y-%m-%dT%H:%M:%SZ")
                videos.append(
                    Video(title=search_result['snippet']['title'],
                          description=search_result['snippet']['description'],
                          id=search_result['id']['videoId'],
                          thumbnail=search_result['snippet']['thumbnails']
                          ['default']['url'],
                          published_at=published_at,
                          channel=search_result['snippet']['channelTitle']))

        return videos, response.get('nextPageToken', None)
    except Exception as e:
        print('Error occurred:', e)
        return None, None


def fetch_youtube_videos():
    global next_token
    videos, next_token = call_api(Config.get_api_key(),
                                  Config.get_predefined_search_query(),
                                  next_token)
    save_all_videos(videos)

def save_all_videos(videos):
    with app.app_context():
        try:
            db.session.bulk_save_objects(videos)
            db.session.commit()
            logging.info("Saved all videos to the database.")
        except Exception as e:
            db.session.rollback()
            logging.error("Error occurred during database saving: %s", str(e))
    
sched = BackgroundScheduler(daemon=True)
sched.add_job(fetch_youtube_videos, 'interval', seconds=5)
sched.start()
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

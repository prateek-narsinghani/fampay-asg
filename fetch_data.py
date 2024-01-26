from apscheduler.schedulers.background import BackgroundScheduler
from config import Config

def fetch_youtube_videos():
    print("fetching " + Config.get_api_key())

sched = BackgroundScheduler(daemon=True)
sched.add_job(fetch_youtube_videos,'interval',seconds=1)
sched.start()
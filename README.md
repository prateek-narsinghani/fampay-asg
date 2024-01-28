# Steps to run the project:

Build container image:
```
docker build -t fampay-youtube:latest .
```

Start the containerized app:
```
docker run --env-file dev.env --name fampay -d -p 8000:5000 --rm fampay-youtube:latest
```


You can then navigate to http://localhost:8000/. Please wait for 10 seconds to let the scheduler run for the first time and fetch some videos.

A working demo can be found on this link: https://drive.google.com/file/d/1hzWtJXX_83r4f_M95EzFxLd_c0QIqPLb/view?usp=drive_link

# Project Description
## Dashboard Feature Description:
  - Search queries can be run upon the title or channel name, and searches for relevant videos. For example, if a search query is "tata prag" and searching is selected for title, it will return videos having tata and prag in their title, for example, "The REPETITION!!! || Gukesh vs Praggnanandhaa || Tata Steel Chess (2024)".
  - The videos can be ordered by published_at in either ascending or descending order.
  - Scroll down at the bottom of the page to see the next page and previous page links.
    
## Tech Stack:
  - Flask
  - Sqlite3
    
## Description of files:
  - `app/app.py`: defines the flask app, db, migration, and load configs.
  - `app/routes.py`: defines the routes for the project.
  - `app/forms.py`: flask form to handle search and ordering of videos.
  - `app/models.py`: Definition of Video table. It also contains utility functions to fetch videos from db.
  - `app/fetch_video_scheduler.py`: Defines a scheduler that runs every 10 seconds and fetches videos from YouTube API and stores them in db.
  - `app/templates`: contains html files.
  - `app/styles`: contains css files.
  - `dev.env`: environment variables such as API keys, number of videos per page, etc can be configured here.
  - `.env`: similar to dev.env but used when running flask locally.
  - `config.py`: loads all the configurations.

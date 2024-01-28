# Steps to run the project:

Build a container image
```
docker build -t fampay-youtube:latest .
```

Start the containerized app <br>
```
docker run --env-file dev.env --name fampay -d -p 8000:5000 --rm fampay-youtube:latest
```


You can then go to `http://localhost:8000/`. Please wait for 10 seconds to let the scheduler run for the first time.

# Project Description
## Tech Stack:
  - Flask
  - Sqlite3
    
## Description of files:
  - `app/app.py`: defines the flask app, db, migration, and load configs.
  - `app/routes.py`: defines the routes for the project.
  - `app/forms.py`: flask form to handle search and ordering of videos.
  - `app/models.py`: Definition of Video table. It also contains utility functions to fetch videos from db.
  - `app/fetch_video_scheduler.py`: Defines a scheduler that runs every 10 seconds and fetches videos from YouTube API and stores them in db.
  - `app/templates`: contains html files
  - `app/styles`: contains css files
  - `dev.env`: environment variables such as API keys, number of videos per page, etc can be configured here.
  - `.env`: similar to .dev.env but used when running flask locally
  - `config.py`: loads all the configurations.

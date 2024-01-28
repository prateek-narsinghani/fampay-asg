<h2>Steps to run the project:</h2>

Build a container image
```
docker build -t fampay-youtube:latest .
```

Start the containerized app <br>
```
docker run --env-file dev.env --name fampay -d -p 8000:5000 --rm fampay-youtube:latest
```

You can then go to `http://localhost:8000/`. Please wait for 10 seconds to let the scheduler run for the first time.

<h2>Project Description</h2>
<h4>Tech Stack:</h4>
<ul>
  <li>Flask</li>
  <li>Sqlite3</li>
</ul>
<h4>Description of main files:</h4>
<ul>
  <li>
    app/app.py: Defines the flask app, db, migration, and load configs.
  </li>
  <li>
    app/routes.py: defines the routes for the project.
  <li>
    app/forms.py: Flask form to handle search and ordering of videos.
  </li>
  <li>
    app/models.py: Definition of Video table. It also contains the utility functions to fetch videos from db.
  </li>
  <li>
    app/fetch_video_scheduler.py: DEfines a scheduler that runs every 10 seconds and fetches videos from YouTube API and stores them in db.
  </li>
</ul>

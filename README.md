Build a container image
```
docker build -t fampay-youtube:latest .
```

Start the containerized app <br>
```
docker run --env-file dev.env --name fampay -d -p 8000:5000 --rm fampay-youtube:latest
```

FROM python:slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY app app
COPY migrations migrations
COPY youtube.py config.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP youtube.py

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
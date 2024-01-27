import queue
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from datetime import datetime
from app import db


class Video(db.Model):
    id: so.Mapped[str] = so.mapped_column(primary_key=True)
    title: so.Mapped[str] = so.mapped_column(index=True)
    description: so.Mapped[str]
    thumbnail: so.Mapped[str]
    published_at: so.Mapped[datetime]
    channel: so.Mapped[str] = so.mapped_column(index=True)

    def __repr__(self):
        return '<Title: {} Channel:{}>'.format(self.title, self.channel)
    
    @staticmethod
    def get_all_videos():
        query = sa.select(Video)
        videos = db.session.scalars(query).all()
        return videos

from datetime import datetime
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

from db import db

Base = declarative_base()


class Posts(db.Model):
    __tablename__ = "posts"
    id = Column(Integer(), primary_key=True)
    title = Column(String(80), unique=True, nullable=False)
    slug = Column(String(30), nullable=False, default="")
    content = Column(String(255), nullable=True)
    published = Column(DateTime, default=datetime.utcnow)
    timestamp = Column(DateTime, default=datetime.utcnow)

    def __init__(self, title, slug, content, published, timestamp):
        self.title = title
        self.slug = slug
        self.content = content
        self.published = published
        self.timestamp = timestamp
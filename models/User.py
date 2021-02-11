from sqlalchemy.sql import func
from dataclasses import dataclass
import datetime
from app import db


@dataclass
class User(db.Model):
    id: int
    username: str
    password: str
    deletedAt: datetime
    updatedAt: datetime
    createdAt: datetime

    __tablename__ = 'user'
    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    deletedAt = db.Column(db.DateTime, name='deleted_at', nullable=True)
    updatedAt = db.Column(db.DateTime, name='updated_at', nullable=False, server_default=func.now(),
                          onupdate=func.now())
    createdAt = db.Column(db.DateTime, name='created_at', nullable=False, server_default=func.now())

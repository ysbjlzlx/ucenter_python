from sqlalchemy.sql import func
from sqlalchemy.ext.hybrid import hybrid_property
from dataclasses import dataclass
import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from app import db


@dataclass
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String(255))
    _password = db.Column('password', db.String(255))
    deletedAt = db.Column(db.DateTime, name='deleted_at', nullable=True)
    updatedAt = db.Column(db.DateTime, name='updated_at', nullable=False, server_default=func.now(),
                          onupdate=func.now())
    createdAt = db.Column(db.DateTime, name='created_at', nullable=False, server_default=func.now())

    id: int
    username: str
    _password: str
    deletedAt: datetime
    updatedAt: datetime
    createdAt: datetime

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    def check_password(self, value):
        return check_password_hash(self.password, value)

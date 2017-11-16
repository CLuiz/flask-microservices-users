import datetime

from project import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active  = db.Column(db.Boolean(), default=False, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init(self, username, email):
        self.username = username
        self.email = email
        self.createed_at = datetime.datetime.utcnow()


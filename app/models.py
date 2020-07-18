from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(120))
    runs = db.relationship('Run', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Run(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    distance_miles = db.Column(db.Float)
    time = db.Column(db.Time)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Run {}>'.format(self.timestamp)
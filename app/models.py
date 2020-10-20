from app import db
from app import login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    """
    This class models a User for the application, with methods to set a password, check it,
    and return a string representation. Data for runs that are Run objects.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(120))
    runs = db.relationship('Run', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Run(db.Model):
    """
    This class models a Run, with an id, timestamp, distance, and associated user. 
    """
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    distance_miles = db.Column(db.Float)
    time = db.Column(db.Time)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Run {}>'.format(self.timestamp)

    # defines comparision of two runs - used to sort runs my date logged
    def __lt__(self, other):
        return self.timestamp < other.timestamp

# load user id from database for flask-login to use


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

from main import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))

    def __repr__(self):
        return '<User {} {}>'.format(self.username, self.email)

class Run(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # TODO: fill out rest of this 
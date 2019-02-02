from __init__ import db

class User(db.Model):
    name = db.Column(db.String, primary_key=True)
    carma = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<User {}>'.format(self.name)

db.create_all()

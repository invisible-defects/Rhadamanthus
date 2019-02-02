from app import db, login
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True)
    surname = db.Column(db.String(64), index=True)
    carma = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '<User {}>'.format(self.name)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

db.create_all()
from flask_sqlalchemy import SQLAlchemy
from Kol import db




# user = User(id = , fname = '', lname = '', username = '', password = '',email = '')

class User(db.Model):
    id = db.Column(db.Integer, nullable = False, primary_key=True)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    username = db.Column(db.String(25), nullable=False, unique=True)
    email = db.Column(db.String(125), nullable=False, unique=True)
    image = db.Column(db.String(20), nullable=False, default = 'default.jpg')
    password = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return f"User('{self.fname}, {self.lname}', '{self.username}', '{self.email}', '{self.image}')"
    

# class productions(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     cost = db.Column(db.Integer, nullable=False)

from Kol import db,Kol
with Kol.app_context():
    db.create_all()
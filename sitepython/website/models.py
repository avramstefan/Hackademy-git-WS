from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

#Reprezintă modelul pentru stocarea notelor în baza de date
class Note(db.Model):
    #id: Cheie primară, un identificator unic pentru fiecare notă
    id = db.Column(db.Integer, primary_key=True)
    #data: Textul notei, cu o limită de 10.000 de caractere
    data = db.Column(db.String(10000))
    #date: Data și ora creării notei, utilizând funcția func.now()
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    #user_id: Cheie străină, care se referă la id-ul utilizatorului care a creat nota, legând astfel nota de utilizatorul respectiv
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#Reprezintă modelul pentru stocarea informațiilor despre utilizatori în baza de date
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
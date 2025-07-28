# models.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from form import Formulario



db = SQLAlchemy()

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    slug = db.Column(db.String(50), nullable=False)
    image1 = db.Column(db.String(200))
    alttitle1 = db.Column(db.String(100))
    image2 = db.Column(db.String(200))
    alttitle2 = db.Column(db.String(100))
    image3 = db.Column(db.String(200))
    alttitle3 = db.Column(db.String(100))
    link1 = db.Column(db.String(200))
    link2 = db.Column(db.String(200))
    frase1 = db.Column(db.String(200), nullable=False)
    frase2 = db.Column(db.String(200), nullable=True)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
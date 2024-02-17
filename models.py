"""Models for adopt app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)

# MODELS #
class Pet(db.Model):
    __tablename__ = "pets"

    id = db.Column(db.Integer, 
                   primary_key=True, 
                   autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Text)
    notes = db.Column(db.Integer)
    available = db.Column(db.Boolean, nullable=False, default=True)


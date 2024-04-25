from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    properties = db.Column(db.String(50), nullable=False)
    price_per_night = db.Column(db.String(50), nullable=False)
    amenities = db.Column(db.String(255), nullable=False)

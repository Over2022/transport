from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import url_for


db = SQLAlchemy()


class Add(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Integer, nullable=False)
    end_date = db.Column(db.Integer, nullable=False)
    city_start = db.Column(db.String(100), nullable=False)
    city_end = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Add %r>' % self.id

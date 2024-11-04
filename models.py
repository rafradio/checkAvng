from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

class MyUser(db.Model):
    __tablename__ = 'myusers'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    second_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    # created_at = db.Column(db.DateTime, default=datetime.utcnow)
    password = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, first_name, second_name, email, password):
        self.first_name = first_name
        self.second_name = second_name
        self.email = email
        self.password = password


    def __repr__(self):
        return f'User({self.second_name}, {self.email})'
    
class Valuty(db.Model):
    __tablename__ = 'valuty'
    id = db.Column(db.Integer, primary_key=True)
    currency_name = db.Column(db.String(80), unique=False, nullable=False)
    byu = db.Column(db.String(80), unique=False, nullable=False)
    sell = db.Column(db.String(120), unique=False, nullable=False)

    def __init__(self, currency_name, byu, sell):
        self.currency_name = currency_name
        self.byu = byu
        self.sell = sell


    def __repr__(self):
        return f'User({self.currency_name}, {self.byu})'
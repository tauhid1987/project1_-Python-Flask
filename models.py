import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    

    def add_review(self, comment):
        c = Reviews(comment=comment, username=self.username)
        db.session.add(c)
        db.session.commit()


class Books(db.Model):
    __tablename__="books"
    isbn = db.Column(db.String, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    year = db.Column(db.CHAR(4), nullable=False)


class Reviews(db.Model):
    __tablename__="reviews"    
    isbn = db.Column(db.String, primary_key=True)
    review = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String, nullable=False)
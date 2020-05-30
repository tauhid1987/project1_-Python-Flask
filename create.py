import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://uojpwnhprhgzqh:bdd53b5759b99c2c96a12c0cc64d5513cb7f528c861833cbfc635204f36ccc62@ec2-34-200-72-77.compute-1.amazonaws.com:5432/db6d25ronj41ru'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
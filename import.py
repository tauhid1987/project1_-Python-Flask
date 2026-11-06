import csv
import os

from flask import Flask, render_template, request
from models import *

DATABASE_URL = os.environ["DATABASE_URL"]  # set in the environment, never commit it
if DATABASE_URL.startswith("postgres://"):   # SQLAlchemy 1.4+ needs the postgresql:// scheme
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():

    f = open("books.csv")
    reader = csv.reader(f)
    header = next(reader)
    for isbn, title, author, year in reader:
        if year == "year":
            print("Skipped The first line which has the column names")
        else:            
            books = Books(isbn = isbn, title= title, author= author, year= year)
            db.session.add(books)
            print(f"Added book with isbn {isbn}.")

    print("Imported Successfully")
    db.session.commit()
    
    

if __name__ == "__main__":
    with app.app_context():
        main()
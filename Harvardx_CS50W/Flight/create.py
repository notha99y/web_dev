import os
from flask import Flask, render_template, request
from models import *
from settings import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
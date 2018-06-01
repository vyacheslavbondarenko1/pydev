from flask import request, session, redirect, render_template
import models
from db import db

from flask.blueprints import Blueprint


home = Blueprint('home', __name__,
                 template_folder='templates',
                 static_folder='static')

@home.route("/")
def index():
    posts = db.session.query(models.Posts).all()
    print posts
    return render_template("index.html", myposts=posts)

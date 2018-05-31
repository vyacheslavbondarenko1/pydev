from flask import request, session, redirect, render_template

from flask.blueprints import Blueprint

home = Blueprint('home', __name__,
                 template_folder='templates',
                 static_folder='static')

@home.route("/")
def index():
    return render_template("index.html")
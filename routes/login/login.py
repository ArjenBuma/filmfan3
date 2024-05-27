"""from flask import Blueprint, render_template, session, request, redirect, url_for

# from ...extensions import db
# from ...models.auction import Auction

from models.regisseur import Regisseur

# from ..auth.auth import login_required, get_user

home = Blueprint("home", __name__, static_folder="static", template_folder="templates")

# https://www.geeksforgeeks.org/retrieving-html-from-data-using-flask
@home.route("/", methods = ["GET", "POST"])
def get():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       email = request.form.get("form_email")
       # getting input with name = lname in HTML form
       password = request.form.get("form_password")
       return "Your details are: " + email + ":" + password
    
    regisseurs = Regisseur.query.all()
    return render_template("Formulier2.html", length=len(regisseurs), regisseurs=regisseurs)

"""

from filmfan import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
# By inheriting the UserMixin we get access to a lot of built-in attributes
# which we will be able to call in our views!
# is_authenticated()
# is_active()
# is_anonymous()
# get_id()


# The user_loader decorator allows flask-login to load the current user
# and grab their id.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
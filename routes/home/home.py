from flask import Blueprint, render_template, session, request, redirect, url_for

# from ...extensions import db
# from ...models.auction import Auction

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
    
   return render_template("home.html")
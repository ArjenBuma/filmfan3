from flask import Blueprint, render_template, session, request, redirect, url_for

from extensions import db
from models.acteur import Acteur

# from ...models.auction import Auction
# from ..auth.auth import login_required, get_user


# Define the blueprint for acteur-related routes
acteur = Blueprint("acteur", __name__, static_folder="static", template_folder="templates")

# Route to get and display all acteurs
@acteur.route("/", methods = ["GET"])
def getActeurs(): 
  acteurs = Acteur.query.all()
  return render_template("acteurs.html", length=len(acteurs), acteurs=acteurs)

# Route to get and display a specific acteur by id
@acteur.route("/<id>", methods = ["GET"])
def getActeur(id):
  acteur = Acteur.query.filter_by(id=id).first()
  return render_template("acteur.html",  acteurs=acteur)



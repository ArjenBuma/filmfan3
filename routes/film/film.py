from flask import Blueprint, render_template, session, request, redirect, url_for

from extensions import db
from models.film import Film
from models.regisseur import Regisseur
from models.acteur import Acteur
from models.rol import Rol


film = Blueprint("film", __name__, static_folder="static", template_folder="templates")


@film.route("/", methods = ["GET"])
def getPageFilms():
    films = []
    regs = []
    rollen = []
    for film, reg in db.session.query(Film, Regisseur).filter(Film.id_regisseur == Regisseur.id).all():
        films.append(film)
        regs.append(reg)

        # returns array of roles related to movie
        gatherdRoles = Rol.query.filter(Rol.id_film == film.id).all()
        # adds array to array
        rollen.append(gatherdRoles)
            
    
    return render_template("films.html", films=films, regs=regs, rollen=rollen)

@film.route("/<id>", methods = ["GET"])
def getPageFilm(id):
    film = Film.query.filter_by(id=id).first()
    
    if film is None:
        print("error")

    reg = Regisseur.query.filter_by(id=film.id_regisseur).first()
    rol = Rol.query.filter_by(id_film=film.id).first()
    
    return render_template("film.html", film=film, reg=reg, rol=rol)

    # rol = Rol.query.filter_by(id=rol.id_film).first()
    # return render_template("film.html", film=film, rol=rol)



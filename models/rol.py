from extensions import db

class Rol(db.Model):
    __tablename__ = "rol"
    id = db.Column(db.Integer, primary_key=True)
    id_acteur = db.Column(db.Integer, db.ForeignKey("acteur.id"))
    id_film = db.Column(db.Integer, db.ForeignKey("film.id"))
    naam_personage = db.Column(db.String, nullable=True)
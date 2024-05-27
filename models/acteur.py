from extensions import db

class Acteur(db.Model):
    __tablename__ = "acteur"
    id = db.Column(db.Integer, primary_key=True)
    voornaam = db.Column(db.String, nullable=True)
    achternaam = db.Column(db.String, nullable=True)
 #   image = db.Colom(db.string, nullable=True)
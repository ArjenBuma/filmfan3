from extensions import db

class Regisseur(db.Model):
    __tablename__ = "regisseur"
    id = db.Column(db.Integer, primary_key=True)
    voornaam = db.Column(db.String, nullable=True)
    achternaam = db.Column(db.String, nullable=True)
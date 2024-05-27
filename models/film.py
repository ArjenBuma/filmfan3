from extensions import db

class Film(db.Model):
    __tablename__ = "film"
    id = db.Column(db.Integer, primary_key=True)
    titel = db.Column(db.String, nullable=True)
    id_regisseur = db.Column(db.Integer, db.ForeignKey("regisseur.id"), nullable=True)
    jaar = db.Column(db.Integer, nullable=True)
    plot = db.Column(db.String, nullable=True)
    # omzet = db.Column(db.Integer, nullable=True)

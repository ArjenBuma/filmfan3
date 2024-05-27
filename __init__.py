import os
from flask import Flask

# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

from routes.home.home import home
from routes.film.film import film
from routes.regisseur.regisseur import regisseur
from routes.acteur.acteur import acteur


from extensions import db

basedir = os.path.abspath(os.path.dirname(__name__))

def create_app():
    app = Flask (__name__)
    
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///filmfan.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SECRET_KEY'] = 'secretkey'
    db.init_app(app)

    with app.app_context():
        db.create_all()
        app.register_blueprint(home, url_prefix="/")
        app.register_blueprint(film, url_prefix="/film")
        app.register_blueprint(regisseur, url_prefix="/regisseur")
        app.register_blueprint(acteur, url_prefix="/acteur")

    return app

app = create_app()
app.run(debug=True)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = "database.db"

# cream aplicatia create_app pentru a fi instanta principala a aplicatiei Flask
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)#Se inițializează baza de date cu aplicația Flask
    
# rutele aplicației și funcționalitățile asociate
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note
    
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

#Verifică dacă baza de date există deja în sistem
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)#Creează toate tabelele bazei de date dacă nu există
        print('Created Database!')
from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
from flask_mail import Mail
from flask_login import LoginManager
db = SQLAlchemy()
mail = Mail()
bootstrap = Bootstrap()
SECRET_KEY = os.urandom(32)
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
MAIL_PASSWORD =os.environ.get("mail_password")

def create_app(config_name):
    app =Flask(__name__)
    app.config.from_object(config_options[config_name])
    app.config['SECRET_KEY'] = 'wangari775'
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    login_manager = LoginManager()
    # login_manager._session_protection ='strong'
    login_manager.login_view = 'views.login'
    login_manager.init_app(app)
    from .views import views
    app.register_blueprint(views, url_prefix= "/")
    from .models import Blogpost
    # @login_manager.user_loader
    # def load_user(user_id):
    #     return User.query.get(int(id))
    return app

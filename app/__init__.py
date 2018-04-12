from flask import Flask, template_rendered
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config 
from flask_login import LoginManager
from flask_moment import Moment
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
moment = Moment()
from .models import User, Role

bootstrap = Bootstrap()
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    bootstrap.init_app(app)
    db.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)
    db.create_all(app=app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

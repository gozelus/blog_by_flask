from flask import Flask, template_rendered
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config 
from .auth import auth as auth_blueprint
db = SQLAlchemy()

bootstrap = Bootstrap()
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    bootstrap.init_app(app)
    db.init_app(app)
    db.create_all(app=app)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    return app

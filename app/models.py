from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    """[summary]
    
    Arguments:
        db {[type]} -- [description]
    
    Raises:
        AttributeError -- [description]
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    # role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))
    @property
    def password(self):
        """[summary]
        
        Raises:
            AttributeError -- [description]
        """
        raise AttributeError('')
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_pwd(self, password):
        return check_password_hash(self.password_hash, password)

        

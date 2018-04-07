from werkzeug.security import generate_password_hash, check_password_hash
from . import db

class User(db.Model):
    """[summary]
    
    Arguments:
        db {[type]} -- [description]
    
    Raises:
        AttributeError -- [description]
    """
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

        

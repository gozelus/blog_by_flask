from functools import wraps
from flask import abort
from flask_login import current_user
from .models import Permission
def perssion_required(permssion):
    def decorator(f):
        @wraps(f)
        def decorated_func(*args, **kwrags):
            if not current_user.can(permssion):
                abort(403)
            return f(*args, **kwrags)
        return decorated_func
    return decorator

def admin_required(f):
    return perssion_required(Permission.ADMINISTER)(f)
from functools import wraps
from flask import abort
from flask_login import current_user


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def biz_logging(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print("%s is called" % func.__name__)
        print("参数1：%s" % (",".join(args)))
        print("参数2：%s" % str(kwargs))
        return func(*args, **kwargs)
    return with_logging



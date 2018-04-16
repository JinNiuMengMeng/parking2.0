from app import db
from flask_login import UserMixin, AnonymousUserMixin
from .. import login_manager


class Role(db.Model):
    __tablename__ = 'usr_role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name


class SysUser(UserMixin, db.Model):
    __tablename__ = 'usr_sys_user'
    id = db.Column(db.String, primary_key=True)
    userName = db.Column(name="user_name", type_=db.String(32), unique=True, index=True)
    password = db.Column(name="password", type_=db.String(32))

    def __repr__(self):
        return '<User %r>' % self.userName

    def verify_password(self, password):
        return self.password == password


@login_manager.user_loader
def load_user(user_id):
    return SysUser.query.get(user_id)



class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False

    def is_administrator(self):
        return False


login_manager.anonymous_user = AnonymousUser

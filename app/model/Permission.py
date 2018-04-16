from app import db
from flask_login import UserMixin

class Role(db.Model):
    __tablename__ = 'usr_role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name


class SysUser(UserMixin, db.Model):
    __tablename__ = 'usr_sys_user'
    id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String(32), unique=True, index=True)

    def __repr__(self):
        return '<SysUser %r>' % self.username

from db import db

class UserModel(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer,primary_key = True,autoincrement=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(100))

    def __init__(self,username,password):
        self.username= username
        self.password=password
    @classmethod
    def find_by_user(cls,username):
        return cls.query.filter_by(username = username).first()
    @classmethod
    def find_by_id(cls,_id):
        return cls.query.filter_by(id = _id).first()

    def add_user(self):
        db.session.add(self)
        db.session.commit()

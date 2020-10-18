from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager,db

db =SQLAlchemy()

class User(db.Model,UserMixin):
    __tablename__= 'users'
    id=db.Column(db.Integer(),primary_key=True)
    username=db.Column(db.String(25),unique=True,nullable=False)
    password=db.Column(db.Text(),nullable=False)

    def create(self):
        db.session.add(self)
        db.session.commit()

    def set_password(self,password):
        self.password=generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password,password)



@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
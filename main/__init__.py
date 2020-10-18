from flask import Flask, render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,login_user,logout_user,current_user
from flask_socketio import SocketIO

app = Flask(__name__)
app.secret_key = 'secret'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://pvgvneqzpomofd:ddea9a0a037cebcaaf16c2ab67ee5edad8c32cb66f1922e4c4c187dbe9809969@ec2-54-86-57-171.compute-1.amazonaws.com:5432/daen3mh5aip61s'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
socketio=SocketIO(app)
login_manager=LoginManager()

login_manager.init_app(app)


from. import routes
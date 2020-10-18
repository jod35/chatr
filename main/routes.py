from .models import User
from flask_login import login_user,logout_user,current_user,login_required
from .forms import LoginForm,RegistrationForm
from .import app,db
from flask import render_template,redirect,url_for
from . import socketio
from flask_socketio import send,emit,join_room,leave_room
from time import strftime,localtime


rooms=["family","friends"]

@app.route('/', methods=['GET', 'POST'])
def index():
    form = RegistrationForm()

    if form.validate_on_submit():
        username=form.username.data
        password=form.password.data

        user_obj=User.query.filter_by(username=username).first()

        
        new_user=User(username=username)

        new_user.set_password(password)

        new_user.create()

        return redirect(url_for('login'))
    context = {
        'form': form
    }
    return render_template('index.html', **context)

@app.route('/login',methods=['GET', 'POST'])
def login():
    form=LoginForm()
    

    username=form.username.data

    password= form.password.data

    user_obj=User.query.filter_by(username=username).first()

    if user_obj and user_obj.check_password(password):
        login_user(user_obj)
        return redirect(url_for('chatroom'))

    

    return render_template('login.html',form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/chatroom')
def chatroom():
    context={
        'username':current_user.username,
        'rooms':rooms

    }
    return render_template('chat.html',**context)

#SocketIO events
@socketio.on('message')
def message(data):
    print(f"\n\n{data}\n\n")
    send({'msg':data['msg'],'username':data['username'],
    'timestamp':strftime('%b-%d %I:%M%p',localtime()),data['room']})
    
    
@socketio.on('join')
def join(data):
    join_room(data['room'])
    send({'msg':data['username'] + "has joined the room " + data['room'] +"room"})

@socketio.on('leave')
def leave(data):
    data['room']
    send({'msg':data['username']+"has left the room " + data['room'] + " room"})

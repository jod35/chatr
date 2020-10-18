from flask import Flask, render_template,redirect,url_for
from forms import RegistrationForm,LoginForm
from models import User
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'secret'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://pvgvneqzpomofd:ddea9a0a037cebcaaf16c2ab67ee5edad8c32cb66f1922e4c4c187dbe9809969@ec2-54-86-57-171.compute-1.amazonaws.com:5432/daen3mh5aip61s'

db=SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = RegistrationForm()

    if form.validate_on_submit():
        username=form.username.data
        password=form.password.data

        user_obj=User.query.filter_by(username=username).first()

        
        new_user=User(username=username,password=password)

        new_user.create()

        return redirect(url_for('login'))
    context = {
        'form': form
    }
    return render_template('index.html', **context)

@app.route('/login',methods=['GET', 'POST'])
def login():
    form=LoginForm()
    

    if form.validate_on_submit():
        return "Logged In"
    return render_template('login.html',form=form)

if __name__ == "__main__":
    app.run(debug=True)

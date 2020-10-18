from flask import Flask, render_template
from forms import RegistrationForm
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

        return "Inserted Into DB!"
    context = {
        'form': form
    }
    return render_template('index.html', **context)


if __name__ == "__main__":
    app.run(debug=True)

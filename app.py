from flask import Flask, render_template
from forms import RegistrationForm

app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = RegistrationForm()

    if form.validate_on_submit():
        return "Create Success"

    context = {
        'form': form
    }
    return render_template('index.html', **context)


if __name__ == "__main__":
    app.run(debug=True)

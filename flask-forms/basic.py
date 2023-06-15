from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


class InfoForm(FlaskForm):
    submit = SubmitField('Click Me!')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InfoForm()

    if form.validate_on_submit():
        flash('You just clicked the button')

        return redirect(url_for('index'))


    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    name = StringField('Name of Pet: ')
    submit = SubmitField('Add Pet: ')

class DelForm(FlaskForm):
    id = IntegerField('Id of Pet to remove: ')
    submit = SubmitField('Remove Pet')
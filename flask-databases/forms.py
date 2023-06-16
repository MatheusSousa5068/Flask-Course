from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddPetForm(FlaskForm):
    name = StringField('Name of Pet: ')
    submit = SubmitField('Add Pet: ')

class DelPetForm(FlaskForm):
    id = IntegerField('Id of Pet to remove: ')
    submit = SubmitField('Remove Pet')

class AddOwnerForm(FlaskForm):
    name = StringField('Your name: ')
    pet_id = IntegerField('Id of your pet: ')
    submit = SubmitField('Add owner')
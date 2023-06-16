import os

from forms import AddForm, DelForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()

db = SQLAlchemy(app)
Migrate(app, db)


class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    # One to Many
    toys = db.relationship('Toy', backref='pets', lazy='dynamic')

    # One to One
    owner = db.relationship('Owner', backref='pets', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f'{self.owner.name} is the owner of {self.name}'

        return f'{self.name} has no owner yet!'

    def report_toys(self):
        print(f'Those are the {self.name} toys:')
        for toy in self.toys:
            print(toy.item_name)


class Toy(db.Model):
    __tablename__ = 'toys'

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.Text)

    pet_id = db.Column(db.Integer, db.ForeignKey('pets.id'))

    def __init__(self, item_name, pet_id):
        self.item_name = item_name
        self.pet_id = pet_id


class Owner(db.Model):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    pet_id = db.Column(db.Integer, db.ForeignKey('pets.id'))

    def __init__(self, name, pet_id):
        self.name = name
        self.pet_id = pet_id


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/add/', methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data

        new_pet = Pet(name)
        db.session.add(new_pet)
        db.session.commit()

        return redirect(url_for('list'))

    return render_template('add.html', form=form)

@app.route('/list/')
def list():
    pets = Pet.query.all()

    return render_template('list.html', pets=pets)


@app.route('/delete/', methods=['GET','POST'])
def delete():
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data
        pet = Pet.query.get(id)

        db.session.delete(pet)
        db.session.commit()

        return redirect(url_for('list'))
    return render_template('delete.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
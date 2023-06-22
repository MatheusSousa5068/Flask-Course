import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from secure_check import authenticate, identity
from flask_jwt import JWT, jwt_required
from flask_migrate import Migrate


app = Flask(__name__)

# Often people will also separate these into a separate config.py file
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)
jwt = JWT(app, authenticate, identity)
api = Api(app)


class Pet(db.Model):
    name = db.Column(db.String(80),primary_key=True)


    def __init__(self,name):
        self.name=name

    def json(self):
        return {'name': self.name}

    def __str__(self):
        return f"{self.name} "


class PetResource(Resource):
    def get(self,name):

        pet = Pet.query.filter_by(name=name).first()

        if pet:
            return pet.json()
        
        return {'name':'not found'}, 404

    def post(self,name):

        pet = Pet(name=name)
        db.session.add(pet)
        db.session.commit()

        return pet.json()


    def delete(self,name):

        pet = Pet.query.filter_by(name=name).first()
        db.session.delete(pet)
        db.session.commit()

        return {'note':'delete successful'}




class AllPets(Resource):

    #@jwt_required()
    def get(self):
        return [pet.json() for pet in Pet.query.all()]


api.add_resource(PetResource, '/pet/<string:name>')
api.add_resource(AllPets,'/pets')

if __name__ == '__main__':
    app.run(debug=True)

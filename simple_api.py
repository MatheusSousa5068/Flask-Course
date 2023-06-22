from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


pets = [
    {'name': 'Rufus'}
]

class PetNames(Resource):
    def get(self, name):
        for pet in pets:
            if pet['name'] == name:
                return pet

        return {'name': None}, 404

    def post(self, name):
        pet = {'name': name}
        pets.append(pet)

        return pet

    
    def delete(self, name):
        for i, pet in enumerate(pets):
            if pet['name'] == name:
                deleted = pets.pop(i)
                return {'note': f'deleted {deleted}'}
        return {'name': None}, 404


class AllNames(Resource):
    def get(self):
        return {'pets': pets}


api.add_resource(PetNames, '/pet/<string:name>')
api.add_resource(AllNames, '/pets/')

if __name__ == "__main__":
    app.run(debug=True)
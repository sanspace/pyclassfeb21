from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Developer(Resource):
    def get(self):
        return {'name': 'raymond'}

api.add_resource(Developer, '/')
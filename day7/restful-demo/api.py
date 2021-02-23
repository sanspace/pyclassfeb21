from flask import Flask, request
from flask_restful  import Api, Resource

app = Flask(__name__)
api = Api(app)

todos = {}

class ToDoSimple(Resource):
    def get(self, todo_id):
        return { todo_id: todos[todo_id]}
    
    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return { todo_id: todos[todo_id]}

api.add_resource(ToDoSimple, '/<string:todo_id>')

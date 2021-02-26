from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Developer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    skill = db.Column(db.String(10), nullable=False)
    experience = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Developer %r>' % self.name

class DeveloperSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        # fields = ('id', 'name', 'skill', 'experience')
        model = Developer

developer_schema = DeveloperSchema()
developers_schema = DeveloperSchema(many=True)

class DeveloperResource(Resource):
    def get(self, dev_id):
        dev = Developer.query.get_or_404(dev_id)
        return developer_schema.dump(dev)
    
    def put(self, dev_id):
        dev = Developer.query.get_or_404(dev_id)
        if 'name' in request.json:
            dev.name = request.json['name']
        if 'skill' in request.json:
            dev.skill = request.json['skill']
        if 'experience' in request.json:
            dev.experience = request.json['experience']
        db.session.commit()
        return developer_schema.dump(dev)
    
    def delete(self, dev_id):
        dev = Developer.query.get_or_404(dev_id)
        db.session.delete(dev)
        db.session.commit()
        return '', 204

class DeveloperList(Resource):
    def get(self):
        devs = Developer.query.all()
        return developers_schema.dump(devs)
    
    def post(self):
        new_dev = Developer(
            name = request.json['name'],
            skill = request.json['skill'],
            experience = request.json['experience'],
        )
        db.session.add(new_dev)
        db.session.commit()
        return developer_schema.dump(new_dev), 201

api.add_resource(DeveloperList, '/developers')
api.add_resource(DeveloperResource, '/developers/<int:dev_id>')

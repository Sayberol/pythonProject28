from flask_restx import Resource, Namespace
from setup_db import db
from models import Director, DirectorSchema

director_ns = Namespace('Directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        rs = db.session.query(Director).all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200


@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    def get(self, rid):
        r = db.session.query(Director).get(rid)
        sm = DirectorSchema().dump(r)
        return sm, 200

from flask_restx import Resource, Namespace
from setup_db import db
from models import Genre, GenreSchema

genre_ns = Namespace('Genres')


@Genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        rs = db.session.query(Genre).all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200


@Genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        g = db.session.query(Genre).get(gid)
        sm = GenreSchema().dump(g)
        return sm, 200

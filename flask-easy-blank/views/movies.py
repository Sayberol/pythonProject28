from flask import request
from flask_restx import Resource, Namespace
from setup_db import db
from models import Movie, MovieSchema

movie_ns = Namespace('Movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        rs = db.session.query(Movie).all()
        res = MovieSchema(many=True).dump(rs)
        return res, 200

    def post(self):
        req_json = request.json
        add_movie = Movie(**req_json)
        with db.session.begin():
            db.session.add(add_movie)
        return "", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        m = db.session.query(Movie).get(mid)
        sm = MovieSchema().dump(m)
        return sm, 200

    def put(self, mid):
        movie = Movie.query.get(mid)
        if not movie:
            return "", 404
        else:
            db.session.update(movie)
            db.session.commit()
            return "", 204

    def delete(self, mid):
        movie = Movie.query.get(mid)
        if not movie:
            return "", 404
        else:
            db.session.delete(movie)
            db.session.commit()
            return "", 204

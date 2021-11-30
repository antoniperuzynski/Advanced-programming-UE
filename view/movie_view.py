from flask_restful import Resource

from services.utils import get_rows_from_csv
from Models.Movie import Movie


class MovieView(Resource):

    def get(self):
        movie_rows = get_rows_from_csv('./data/movies.csv')
        return [Movie(row[0], row[1], row[2]).__dict__ for row in movie_rows]
from flask_restful import Resource

from Models.Links import Links
from services.utils import get_rows_from_csv


class LinkView(Resource):

    def get(self):
        link_rows = get_rows_from_csv('./data/links.csv')
        return [Links(row[0], row[1], row[2]).__dict__ for row in link_rows]
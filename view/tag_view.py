from flask_restful import Resource

from Models.Tags import Tags
from services.utils import get_rows_from_csv


class TagView(Resource):

    def get(self):
        tag_rows = get_rows_from_csv('./data/tags.csv')
        return [Tags(row[0], row[1], row[2], row[3]).__dict__ for row in tag_rows]
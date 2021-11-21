from flask import Flask
from flask_restful import Resource, Api
import services.utils
import Models.Movie

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        file = services.utils.readfile(r'D:\Antoni\Ue\Programowanie\Lab7\data\movies.csv')
        splitfile = file.split('\n')
        splitfile.pop(0)
        splitfile.pop(len(splitfile)-1)
        listOfFilms = []
        for movies in splitfile:
            movie = movies.split(',')
            listOfFilms.append(Models.Movie.Movie(movie[0], movie[1], movie[2]).__dict__)
        return listOfFilms


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)

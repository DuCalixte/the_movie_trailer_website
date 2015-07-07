# Author: Stanley Calixte
# Project: Project 1 - Movie Trailer Website


import json

from movie import Movie
import fresh_tomatoes

""" Media information is imported from a json file with my favorite movies. """

with open('movie_database.json') as movies_file:
    json_obj = json.load(movies_file)

movies = []
for movie_info in json_obj["movies"]:
    movies.append(Movie(**movie_info))

""" Calling method to create movie site with data """
fresh_tomatoes.open_movies_page(movies)

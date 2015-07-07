# Author: Stanley Calixte
# Project: Project 1 - Movie Trailer Website

class Movie():
	""" A class property providing information about a movie.

	Attributes:
		title: [String], the title of the movie.
		rating: [String], the rating of the movie.
		year: [Integer], the year the movie was released.
		info: [String], a short description of the movie.
		poster_image_url: [String], the url for the poster image of the movie.
		trailer_youtube_url: [String], the url for the youtube trailer of the movie.
		duration: [Integer], the duration of the movie or the total minutes the movie will last.

	"""

	def __init__(self, movie_title, movie_rating, movie_year, movie_info, poster_image, trailer_youtube, movie_duration):
		""" Initializes the class with attributes as described in class. """
		self.title = movie_title
		self.rating = movie_rating
		self.year = movie_year
		self.info = movie_info
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.duration = movie_duration

	def __init__(self, **args):
		""" Initializes the class with attributes as described in class. the argurments are sent as json objects """
		for keyword in ["title", "rating", "year", "info", "poster_image_url", "trailer_youtube_url", "duration"]:
			setattr(self, keyword, args[keyword])
# Author: Stanley Calixte
# Project: Project 1 - Movie Trailer Website


class Movie():
    """ A class property providing information about a movie.
Attributes:
title: [String], the title of the movie.
ating: [String], the rating of the movie.
year: [Integer], the year the movie was released.
info: [String], a short description of the movie.
poster_image_url: [String], the url for the poster image of the movie.
trailer_youtube_url: [String], the url for the youtube trailer of the movie.
duration: [Integer], the duration of the movie or its total minutes."""

    def __init__(self, title, rating, year, info, image, youtube, duration):
        """ Initializes the class with attributes as described in class. """
        self.title = title
        self.rating = rating
        self.year = year
        self.info = info
        self.poster_image_url = image
        self.trailer_youtube_url = youtube
        self.duration = duration

    def __init__(self, **args):
        """
            Initializes the class with attributes as described in class.
            The argurments are sent as json objects """

        for keyword in [
            "title",
            "rating",
            "year",
            "info",
            "poster_image_url",
            "trailer_youtube_url",
            "duration"
        ]:
            setattr(self, keyword, args[keyword])

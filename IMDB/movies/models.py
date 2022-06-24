from django.db import models

class Movie(models.Model):
    """ Movie Model """

    title = models.CharField(
        max_length = 255,
        name = 'title',
        help_text = 'Title of the movie',
        unique = True,
        null = False,
    )

    imdb_rating = models.FloatField(
        name = 'imdb_rating',
        help_text = 'IMDB rating of the movie',
        null = False,
    )

    year = models.IntegerField(
        name = 'year',
        help_text = 'Year of the movie',
        null = False,
    )

    released = models.IntegerField(
        name = 'released',
        help_text = 'Released date of the movie',
        null = False,
    )

    runtime = models.IntegerField(
        name = 'runtime',
        help_text = 'Runtime of the movie',
        null = False,
    )

    genre = models.IntegerField(
        name = 'genre',
        help_text = 'Genre of the movie',
        null = False,
    )

    rated = models.CharField(
        max_length = 5,
        name = 'rated',
        help_text = 'Parental guide of the movie',
        null = True,        
    )

    plot = models.TextField(
        name = 'plot',
        help_text = 'Plot of the movie',
        null = False,        
    )

    director = models.CharField(
        max_length = 100,
        name = 'director',
        help_text = 'Director(s) of the movie',
        null = False,
    )

    writer = models.CharField(
        max_length = 100,
        name = 'writer',
        help_text = 'Writer(s) of the movie',
        null = False,
    )

    actors = models.CharField(
        max_length = 255,
        name = 'actors',
        help_text = 'Actors and Actresses of the movie',
        null = False,
    )

    language = models.CharField(
        max_length = 255,
        name = 'language',
        help_text = 'Language and Actresses of the movie',
        null = False,
    )

    poster_url = models.CharField(
        max_length = 255,
        name = 'poster_url',
        help_text = 'Poster URL of the movie',
        null = False,
    )

    country = models.CharField(
        max_length = 255,
        name = 'country',
        help_text = 'Country of the movie',
        null = False,
    )

    box_office = models.CharField(
        max_length = 255,
        name = 'box_office',
        help_text = 'BoxOffice of the movie',
        null = False,
    )
from django.db import models

class Movie(models.Model):
    """ Movie Model """

    title = models.CharField(
        max_length = 255,
        name = 'title',
        help_text = 'Title of the movie',
    )

    imdb_rating = models.CharField(
        max_length = 20,
        name = 'imdb_rating',
        help_text = 'IMDB rating of the movie',
    )

    year = models.IntegerField(
        name = 'year',
        help_text = 'Year of the movie',
    )

    released = models.CharField(
        max_length = 30,
        name = 'released',
        help_text = 'Released date of the movie',
    )

    runtime = models.CharField(
        max_length = 30,
        name = 'runtime',
        help_text = 'Runtime of the movie',
    )

    genre = models.CharField(
        max_length = 30,
        name = 'genre',
        help_text = 'Genre of the movie',
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
    )

    director = models.CharField(
        max_length = 100,
        name = 'director',
        help_text = 'Director(s) of the movie',
    )

    writer = models.CharField(
        max_length = 100,
        name = 'writer',
        help_text = 'Writer(s) of the movie',
    )

    actors = models.CharField(
        max_length = 255,
        name = 'actors',
        help_text = 'Actors and Actresses of the movie',
    )

    language = models.CharField(
        max_length = 255,
        name = 'language',
        help_text = 'Language and Actresses of the movie',
    )

    poster_url = models.CharField(
        max_length = 255,
        name = 'poster_url',
        help_text = 'Poster URL of the movie',
    )

    country = models.CharField(
        max_length = 255,
        name = 'country',
        help_text = 'Country of the movie',
    )

    box_office = models.CharField(
        max_length = 255,
        name = 'box_office',
        help_text = 'BoxOffice of the movie',
    )
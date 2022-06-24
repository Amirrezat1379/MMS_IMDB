import os
from django.http import HttpResponse
import requests
from dotenv import load_dotenv
from django.shortcuts import render

from movies.models import Movie


MOVIE_TITLES = [
    'The Shawshank Redemption',
    'The Godfather',
    'The Dark Knight',
    'The Godfather Part II',
    '12 Angry Men',
    'Schindler\'s List'
]


def index(request):

    # In case no data is already available, insert them
    if len(Movie.objects.all()) == 0:
        fill_db()

    context = {'movies': Movie.objects.all()}
    return render(request, 'index/index.html', context)


def movie(request, id):
    return render(request, 'index/movie.html', {})


def fill_db():
    
    load_dotenv()   # take environment variables from .env

    OMDB_SECRET = os.environ.get("OMDB_SECRET") # OMDB API key

    # Fetch movie info using the OMDB API
    for title in MOVIE_TITLES:
        info = requests.get('http://www.omdbapi.com/', params = {
            'apikey': OMDB_SECRET,
            't': title,
            'plot': 'full'
        }).json()

        # Create a new movie object
        Movie(
            title = info['Title'],
            imdb_rating = info['Ratings'][0]['Value'],
            year = info['Year'],
            rated = info['Rated'],
            plot = info['Plot'],
            director = info['Director'],
            writer = info['Writer'],
            actors = info['Actors'],
            language = info['Language'],
            poster_url = info['Poster'],
            runtime = info['Runtime'],
            genre = info['Genre'],
            released = info['Released'],
            country = info['Country'],
            box_office = info['BoxOffice'],
        ).save()
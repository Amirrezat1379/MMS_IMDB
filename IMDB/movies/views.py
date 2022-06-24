from .models import Movie
from .serializers import MovieSerializer
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def index(request, id = None):

    # Return all movies
    if id is None:
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many = True)

    # Return specific movie
    else:
        movie = get_object_or_404(Movie, id = id)
        serializer = MovieSerializer(movie)
            
    return Response(serializer.data)
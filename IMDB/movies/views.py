from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return render(request, 'movies/index.html')
    return HttpResponse('Hello World!')
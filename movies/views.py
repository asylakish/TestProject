from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from movies.models import MoviesMovie

def movie_list_view(request: HttpRequest) -> HttpResponse:
    movies = MoviesMovie.objects.all()[:4]

    context = {
        'movies': movies
    }
    return render(request, 'movies/movie_list.html', context)


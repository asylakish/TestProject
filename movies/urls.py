from django.urls import path

from movies import views


app_name = 'movies'

urlpatterns = [
    path('', views.movie_list_view, name='home')
]

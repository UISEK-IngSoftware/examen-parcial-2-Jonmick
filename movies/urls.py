from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("", views.index, name="index"),
    path("movies/<int:id>/", views.movie_details, name="movie_details"),
    path("movie/add/", views.add_movie, name="add_movie"),
]

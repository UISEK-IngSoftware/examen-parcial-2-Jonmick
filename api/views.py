from rest_framework import viewsets
from movies.models import Movie
from .serializers import MovieSerializers

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.order_by('title')
    serializer_class = MovieSerializers


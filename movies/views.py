from rest_framework import generics

from .models import Movie
from .serializer import MovieSerializer


class MovieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    

class MovieRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    def get_object(self):
        uuid = self.kwargs.get('uuid')
        movie = Movie.objects.get(pk=uuid)
        return movie
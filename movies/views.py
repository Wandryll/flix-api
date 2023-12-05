from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import generics

from django.http import Http404

from .models import Movie
from .serializer import MovieSerializer

import uuid


class MovieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    

class MovieRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    def get_object(self):
        movie_uuid = self.kwargs.get('movie_uuid')
        
        try:
            valid_uuid = uuid.UUID(movie_uuid)
        except ValueError:
            raise ValidationError('filme não encontrado.')
        
        try:
            movie = Movie.objects.get(pk=movie_uuid)
            return movie
        except Movie.DoesNotExist:
            raise Http404('filme não encontrado.')
        
    def get(self, *args, **kwargs):
        try:
            movie = self.get_object()
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
        except Http404:
            return Response({'detail': 'filme não encontrado.'}, status=404)
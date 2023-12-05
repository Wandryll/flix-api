from django.http import Http404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.validators import ValidationError

from .models import Genre
from .serializers import GenreSerializer

import uuid


class GenreListCreateAPIView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    

class GenreRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    
    def get_object(self):
        genre_uuid = self.kwargs.get('genre_uuid')
        
        try:
            valid_uuid = uuid.UUID(genre_uuid)
        except ValueError:
            raise ValidationError('gênero não encontrado')
            
        try:
            genre = Genre.objects.get(pk=genre_uuid)
            return genre
            
        except Genre.DoesNotExist:
            raise Http404('gênero não encontrado')
        
    def get(self, *args, **kwargs):
        try: 
            genre = self.get_object()
            serializer = GenreSerializer(genre)
            return Response(serializer.data)
        
        except Http404 as e:
            return Response({'detail': 'gênero não encontrado.'})
from django.http import Http404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .models import Actor
from .serializers import ActorSerializer

import uuid


class ActorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    

class ActorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    
    def get_object(self):
       
        actor_uuid = self.kwargs.get('actor_uuid')
        
        try:
            uuid_obj = uuid.UUID(actor_uuid)
            
        except ValueError:
            raise ValidationError({'detail': 'ator não encontrado.'})
        
        try:
            actor = Actor.objects.get(pk=actor_uuid)
            return actor
        
        except Actor.DoesNotExist:
            raise Http404('ator não encontrado.')
        
    def get(self, *args, **kwargs):
        
        try:
            actor = self.get_object()
            serializer = ActorSerializer(actor)
            return Response(serializer.data)
        
        except Http404 as e:
            return Response({'detail': str(e)}, status=404)
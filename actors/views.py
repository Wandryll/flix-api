from rest_framework import generics

from .models import Actor
from .serializers import ActorSerializer


class ActorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    

class ActorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    
    def get_object(self):
        uuid = self.kwargs.get('uuid')
        
        actor = Actor.objects.get(pk=uuid)
        return actor
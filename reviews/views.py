from rest_framework import generics
from rest_framework.response import Response
from rest_framework.validators import ValidationError
from django.http import Http404

from .models import Review
from .serializer import ReviewSerializer

import uuid


class ReviewListCrateAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    
class ReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get_object(self):
        review_uuid = self.kwargs.get('review_uuid')
        
        try:
            uuid_valid = uuid.UUID(review_uuid)
        except ValueError:
            raise ValidationError('review não encontrada.')
        try:
            review = Review.objects.get(pk=review_uuid)
            return review
        except Review.DoesNotExist:
            return Http404('review não encontrada.')
        
    def get(self, *args, **kwargs):
        try:
            review = self.get_object()
            serializer = ReviewSerializer(review)
            return Response(serializer.data)
        except Http404:
            return Response({"detail": "review não encontrada."}, status=404)
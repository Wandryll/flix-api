from django.urls import path

from .views import ActorListCreateAPIView, ActorRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('actors/', ActorListCreateAPIView.as_view(), name='actors-create-list'),
    path('actor/<uuid:uuid>/', ActorRetrieveUpdateDestroyAPIView.as_view(), name='actors-detail')

]
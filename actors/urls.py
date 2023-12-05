from django.urls import path

from .views import ActorListCreateAPIView, ActorRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('actors/', ActorListCreateAPIView.as_view(), name='actors-create-list'),
    path('actor/<str:actor_uuid>/', ActorRetrieveUpdateDestroyAPIView.as_view(), name='actors-detail')

]
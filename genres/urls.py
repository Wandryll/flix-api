from django.urls import path

from .views import GenreListCreateAPIView, GenreRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('genres/', GenreListCreateAPIView.as_view(), name='genre-create-list'),
    path('genre/<int:pk>', GenreRetrieveUpdateDestroyAPIView.as_view(), name='genre-detail')
]
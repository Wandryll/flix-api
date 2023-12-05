from django.urls import path

from .views import MovieListCreateAPIView, MovieRetriveUpdateDestroyAPIView


urlpatterns = [
    path('movies/', MovieListCreateAPIView.as_view(), name='movie-create-list'),
    path('movie/<str:movie_uuid>/', MovieRetriveUpdateDestroyAPIView.as_view(), name='movie-detail')
]
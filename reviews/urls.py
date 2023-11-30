from django.urls import path

from .views import ReviewListCrateAPIView, ReviewRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('reviews/', ReviewListCrateAPIView.as_view(), name='review-list-create'),
    path('review/<int:pk>', ReviewRetrieveUpdateDestroyAPIView.as_view(), name='review-detail')
]
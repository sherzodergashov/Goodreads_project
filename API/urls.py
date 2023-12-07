from django.urls import path
from API.views import BookReviewAPIView, BookAPIReviewsView


app_name = 'API'
urlpatterns = [
    path('reviews/<int:id>/', BookReviewAPIView.as_view(), name='reviews-api'),
    path('list/', BookAPIReviewsView.as_view(), name='reviews-list-api'),
]


from django.urls import path
from API.views import BookReviewAPIView, BookAPIReviewsView, OrderViewAPI, OrdersAPIView


app_name = 'API'
urlpatterns = [
    path('reviews/<int:id>/', BookReviewAPIView.as_view(), name='reviews-api'),
    path('list/', BookAPIReviewsView.as_view(), name='reviews-list-api'),
    path('order/<int:id>/', OrdersAPIView.as_view(), name='order-api'),
    path('order/list', OrderViewAPI.as_view(), name='order-list-api'),
]


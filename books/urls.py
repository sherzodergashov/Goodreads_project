from django.urls import path

from books.views import BooksView, BookDatailView, AddReviewView, \
    EditReviewView, ConfirmDeleteReviewView, DeleteReviewView, \
    BlogView, NewsView, WishListView, CartView, CategorieView, CategoriesIDView

app_name = "books"
urlpatterns = [
    path("", BooksView.as_view(), name='list'),
    path("<int:id>/", BookDatailView.as_view(), name='datail'),
    path("<int:id>/reviews/", AddReviewView.as_view(), name='reviews'),
    path("<int:book_id>/reviews/<int:review_id>/edit/", EditReviewView.as_view(), name='edit-review'),
    path("<int:book_id>/reviews/<int:review_id>/delete/confirm/",
         ConfirmDeleteReviewView.as_view(),
         name='confirm-delete-review'),
    path("<int:book_id>/reviews/<int:review_id>/delete/review/",
         DeleteReviewView.as_view(),
         name='delete-review'),
    path('blog/', BlogView, name='blog'),
    path('blog/news/', NewsView, name='new'),
    path('wishlist/', WishListView, name='wishlist'),
    path('cart/', CartView, name='cart'),
    path('categories/', CategorieView, name='categories'),
    path('categories/<int:id>/', CategoriesIDView.as_view(), name='type'),

]

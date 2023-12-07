from django.test import TestCase
from django.urls import reverse

from books.models import Book, BookReview
from users.models import CustomUser


class HomePageTestCase(TestCase):
    def test_paginated_list(self):
        book = Book.objects.create(title="book1", description="description1", isbn="123123")
        user = CustomUser.objects.create_user(
            username="Sherzod740",
            first_name="Sherzod",
            last_name="Ergashov",
            email="sherzodergashov740@gmail.com"
        )
        user.set_password("123456789")
        user.save()

        review1 = BookReview.objects.create(book=book, user=user, stars_given=3, commend="Very good book")
        review2 = BookReview.objects.create(book=book, user=user, stars_given=4, commend="Useful book")
        review3 = BookReview.objects.create(book=book, user=user, stars_given=5, commend="good book")

        response = self.client.get(reverse("home_pages") + "?page_size=2")

        self.assertContains(response, review3.commend)
        self.assertContains(response, review2.commend)
        self.assertNotContains(response, review1.commend)

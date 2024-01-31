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

        review1 = BookReview.objects.create(book=book, user=user, stars_given=3, commend="good not book")
        review2 = BookReview.objects.create(book=book, user=user, stars_given=4, commend="Useful book")
        review3 = BookReview.objects.create(book=book, user=user, stars_given=5, commend="very good book")

        response = self.client.get(reverse("home_pages") + "?page_size=2")

        self.assertContains(response, review3.commend)
        self.assertContains(response, review2.commend)
        self.assertNotContains(response, review1.commend)

class BookRandomTestCase(TestCase):
    def test_book_list(self):
        book1 = Book.objects.create(title="book1", description="description1", isbn="123123")
        book2 = Book.objects.create(title="book2", description="description2", isbn="121212")
        book3 = Book.objects.create(title="book3", description="description3", isbn="000020")

        response = self.client.get("helloworld")

        # books = Book.objects.all()
        for book in [book1, book2]:
            self.assertContains(response, book.title)
        self.assertNotContains(response, book3.title)

        response = self.client.get()

        self.assertContains(response, book3.title)

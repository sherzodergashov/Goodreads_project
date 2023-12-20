from django.test import TestCase
from django.urls import reverse

from books.models import Book, Auther
from users.models import CustomUser


class BooksTestCase(TestCase):
    def test_no_books(self):
        response = self.client.get()

        self.assertContains(response, "No book found.")

    def test_book_list(self):
        book1 = Book.objects.create(title="book1", description="description1", isbn="123123")
        book2 = Book.objects.create(title="book2", description="description2", isbn="121212")
        book3 = Book.objects.create(title="book3", description="description3", isbn="000020")

        response = self.client.get()

        # books = Book.objects.all()
        for book in [book1, book2]:
            self.assertContains(response, book.title)
        self.assertNotContains(response, book3.title)

        response = self.client.get()

        self.assertContains(response, book3.title)

    def test_title_detail(self):
        book = Book.objects.create(title="book", description="description", isbn="123456")
        auther = Auther.objects.create(first_name='Sherzod', last_name='Ergashov')

        response = self.client.get()

        self.assertContains(response, book.title)
        self.assertContains(response, book.description)

        self.assertContains(response, auther.first_name)
        self.assertContains(response, auther.last_name)


    def test_search_books(self):
        book1 = Book.objects.create(title="sport", description="description1", isbn="123123")
        book2 = Book.objects.create(title="news", description="description2", isbn="121212")
        book3 = Book.objects.create(title="history", description="description3", isbn="000020")

        resource = self.client.get()
        self.assertContains(resource, book1.title)
        self.assertNotContains(resource, book2.title)
        self.assertNotContains(resource, book3.title)

        resource = self.client.get()
        self.assertContains(resource, book2.title)
        self.assertNotContains(resource, book1.title)
        self.assertNotContains(resource, book3.title)

        resource = self.client.get()
        self.assertContains(resource, book3.title)
        self.assertNotContains(resource, book1.title)
        self.assertNotContains(resource, book2.title)

class AddReviewTest(TestCase):
    def test_add_review(self):
        book = Book.objects.create(title="book", description="description", isbn="123456")

        user = CustomUser.objects.create_user(
            username="Sherzod740",
            first_name="Sherzod",
            last_name="Ergashov",
            email="sherzodergashov740@gmail.com"
        )
        user.set_password("123456789")
        user.save()
        self.client.login(username="Sherzod740", password="123456789")

        response = self.client.post(reverse("books:reviews", kwargs={"id": book.id}), data={
            "stars_given": 3,
            "commend": "The Pilot's Daughter"
        })
        book_reviews = book.bookreview_set.all()

        self.assertEqual(book_reviews.count(), 1)
        self.assertEqual(book_reviews[0].stars_given, 3)
        self.assertEqual(book_reviews[0].commend, "The Pilot's Daughter")
        self.assertEqual(book_reviews[0].book, book)
        self.assertEqual(book_reviews[0].user, user)


class BookEditReviewTest(TestCase):
    def test_edit_review(self):
        book = Book.objects.create(title="book", description="description", isbn="123456")

        user = CustomUser.objects.create_user(
            username="Sherzod740",
            first_name="Sherzod",
            last_name="Ergashov",
            email="sherzodergashov740@gmail.com"
        )
        user.set_password("123456789")
        user.save()
        self.client.login(username="Sherzod740", password="123456789")

        response = self.client.post(reverse("books:reviews", kwargs={"id": book.id}), data={
            "stars_given": 3,
            "commend": "The Pilot's Daughter"
        })
        book_reviews = book.bookreview_set.all()

        self.assertEqual(book_reviews.count(), 1)
        self.assertNotEqual(book_reviews[0].stars_given, 4)
        self.assertNotEqual(book_reviews[0].commend, "The Pilot's Daughter.")
        self.assertEqual(book_reviews[0].book, book)
        self.assertEqual(book_reviews[0].user, user)



from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from books.models import Book, BookReview
from users.models import CustomUser


class BookReviewAPITestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username="sherzod0101", first_name="Sherzod")
        self.user.set_password("love74013")
        self.user.save()
        self.client.login(username='sherzod0101', password='love74013')

    def test_book_review_detail(self):
        book = Book.objects.create(title="book1", description="description1", isbn="123123")
        br = BookReview.objects.create(book=book, user=self.user, stars_given=5, commend='Very good book')

        response = self.client.get()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], br.id)
        self.assertEqual(response.data['stars_given'], 5)
        self.assertEqual(response.data['commend'], 'Very good book')
        self.assertEqual(response.data['book']['id'], br.book.id)
        self.assertEqual(response.data['book']['title'], 'book1')
        self.assertEqual(response.data['book']['description'], 'description1')
        self.assertEqual(response.data['user']['id'], br.user.id)
        self.assertEqual(response.data['user']['first_name'], 'Sherzod')
        self.assertEqual(response.data['user']['username'], 'sherzod0101')

    def test_book_list_apiview(self):
        user_two = CustomUser.objects.create_user(username="somebady", first_name="Somebady")
        book = Book.objects.create(title="book1", description="description1", isbn="123123")
        br = BookReview.objects.create(book=book, user=self.user, stars_given=5, commend='Very good book')
        br_two = BookReview.objects.create(book=book, user=user_two, stars_given=3, commend='Not book')

        response = self.client.get()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['count'], 2)
        self.assertIn('next', response.data)
        self.assertIn('previous', response.data)
        self.assertEqual(response.data['results'][0]['id'], br_two.id)
        self.assertEqual(response.data['results'][0]['stars_given'], br_two.stars_given)
        self.assertEqual(response.data['results'][0]['commend'], br_two.commend)
        self.assertEqual(response.data['results'][1]['id'], br.id)
        self.assertEqual(response.data['results'][1]['stars_given'], br.stars_given)
        self.assertEqual(response.data['results'][1]['commend'], br.commend)




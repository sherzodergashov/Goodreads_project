from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from books.models import Book, BookReview, Type, Order
from users.models import CustomUser


class BookReviewAPITestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username="sherzod0101", first_name="Sherzod")
        self.user.set_password("love74013")
        self.user.save()
        self.client.login(username='sherzod0101', password='love74013')

    def test_book_review_detail(self):
        book = Book.objects.create(
            title="book1",
            description="description1",
            isbn="123123",
            cover_picture="/media/Humble_Pi_uCayJNG.jpg",
            price="1000.00",
            language="english",
            type=Type.objects.create(
                name='Science Fiction'
            )
        )
        br = BookReview.objects.create(book=book, user=self.user, stars_given=5, commend='Very good book')

        response = self.client.get(reverse('API:reviews-api', kwargs={'id': br.id}))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], br.id)
        self.assertEqual(response.data['stars_given'], 5)
        self.assertEqual(response.data['commend'], 'Very good book')
        self.assertEqual(response.data['book']['id'], br.book.id)
        self.assertEqual(response.data['book']['title'], 'book1')
        self.assertEqual(response.data['book']['description'], 'description1')
        self.assertEqual(response.data['book']['isbn'], '123123')
        self.assertEqual(response.data['book']['cover_picture'], '/media/media/Humble_Pi_uCayJNG.jpg')
        self.assertEqual(response.data['book']['price'], '1000.00')
        self.assertEqual(response.data['book']['language'], 'english')
        self.assertEqual(response.data['book']['type']['name'], 'Science Fiction')
        self.assertEqual(response.data['user']['id'], br.user.id)
        self.assertEqual(response.data['user']['first_name'], 'Sherzod')
        self.assertEqual(response.data['user']['username'], 'sherzod0101')

    def test_book_list_apiview(self):
        user_two = CustomUser.objects.create_user(username="somebady", first_name="Somebady")
        book = Book.objects.create(title="book1", description="description1", isbn="123123")
        br = BookReview.objects.create(book=book, user=self.user, stars_given=5, commend='Very good book')
        br_two = BookReview.objects.create(book=book, user=user_two, stars_given=3, commend='Not book')

        response = self.client.get(reverse('API:reviews-list-api'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['count'], 2)
        self.assertIn('next', response.data)
        self.assertIn('previous', response.data)
        self.assertEqual(response.data['results'][0]['id'], br.id)
        self.assertEqual(response.data['results'][0]['stars_given'], br.stars_given)
        self.assertEqual(response.data['results'][0]['commend'], br.commend)
        self.assertEqual(response.data['results'][1]['id'], br_two.id)
        self.assertEqual(response.data['results'][1]['stars_given'], br_two.stars_given)
        self.assertEqual(response.data['results'][1]['commend'], br_two.commend)

class OrderAPITestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username="sherzod0101", first_name="Sherzod")
        self.user.set_password("love74013")
        self.user.save()
        self.client.login(username='sherzod0101', password='love74013')

    def test_order_api_view(self):
        book = Book.objects.create(
            title="book1",
            description="description1",
            isbn="123123",
            cover_picture="/media/Humble_Pi_uCayJNG.jpg",
            price="1000.00",
            language="english",
            type=Type.objects.create(
                name='Science Fiction'
            )
        )
        order = Order.objects.create(book=book, user=self.user, count=0, date='2023-12-14T22:57:21.703143+05:00')

        response = self.client.get(reverse("API:order-api", kwargs={'id': order.id}))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], order.id)
        self.assertEqual(response.data['book']['id'], order.book.id)
        self.assertEqual(response.data['book']['title'], 'book1')
        self.assertEqual(response.data['book']['description'], 'description1')
        self.assertEqual(response.data['book']['isbn'], '123123')
        self.assertEqual(response.data['book']['cover_picture'], '/media/media/Humble_Pi_uCayJNG.jpg')
        self.assertEqual(response.data['book']['price'], '1000.00')
        self.assertEqual(response.data['book']['language'], 'english')
        self.assertEqual(response.data['book']['type']['name'], 'Science Fiction')
        self.assertEqual(response.data['user']['id'], order.user.id)
        self.assertEqual(response.data['user']['username'], 'sherzod0101')
        self.assertEqual(response.data['user']['first_name'], 'Sherzod')
        self.assertEqual(response.data['count'], 0)
        self.assertNotEquals(response.data['date'], "2024-12-12023-12-14T22:57:21.703143+05:004")

    def test_order_list(self):
        user_two = CustomUser.objects.create_user(username="somebady", first_name="Somebady")
        book = Book.objects.create(
            title="book1",
            description="description1",
            isbn="123123",
            cover_picture="/media/Humble_Pi_uCayJNG.jpg",
            price="1000.00",
            language="english",
            type=Type.objects.create(
                name='Science Fiction'
            )
        )
        order = Order.objects.create(book=book, user=self.user, count=0, date='2023-12-14T22:57:21.703143+05:00')
        order_two = Order.objects.create(book=book, user=user_two, count=1, date='2024-02-01T11:58:28.498592+05:00')

        response = self.client.get(reverse('API:order-list-api'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['count'], 2)
        self.assertIn('next', response.data)
        self.assertIn('previous', response.data)
        self.assertEqual(response.data['results'][0]['id'], order.id)
        self.assertEqual(response.data['results'][0]['count'], order.count)
        self.assertNotEqual(response.data['results'][0]['date'], order.date)
        self.assertEqual(response.data['results'][1]['id'], order_two.id)
        self.assertEqual(response.data['results'][1]['count'], order_two.count)
        self.assertNotEqual(response.data['results'][1]['date'], order_two.date)


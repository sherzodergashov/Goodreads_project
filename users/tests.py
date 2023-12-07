from django.contrib.auth import get_user
from users.models import CustomUser
from django.test import TestCase
from django.urls import reverse




class RegisterTestCase(TestCase):
    def test_user_account_is_created(self):
        self.client.post(
            reverse("users:register"),
            data={
                "username": "sherzodergashov ",
                "first_name": "Sherzod",
                "last_name": "Ergashov",
                "email": "sherzodergashov@gmail.com",
                "password": "sher4501",
                # "address": "Sirdaryo viloyati Yengiyer shahri T.Malik mahallasi 10-uy 2-xonadon",
                # "phone": "+998933204501"
            }
        )

        user = CustomUser.objects.get(username="sherzodergashov")

        self.assertEqual(user.first_name, 'Sherzod')
        self.assertEqual(user.last_name, 'Ergashov')
        self.assertEqual(user.email, 'sherzodergashov@gmail.com')
        self.assertNotEqual(user.password, 'sher4501')
        self.assertTrue(user.check_password("sher4501"))
        # self.assertEqual(user.address, 'Sirdaryo viloyati Yengiyer shahri T.Malik mahallasi 10-uy 2-xonadon')
        # self.assertEqual(user.phone, '+998933204501')

    def test_required_fields(self):
        response = self.client.post(
            reverse("users:register"),
            data={
                "first_name": "Sherzod",
                "email": "sherzodergashov@gmail.com"
            }
        )

        user_count = CustomUser.objects.count()

        self.assertEqual(user_count, 0)
        self.assertFormError(response, "form", "username", "This field is required.")
        self.assertFormError(response, "form", "password", "This field is required.")

    def test_invalid_email(self):
        response = self.client.post(
            reverse("users:register"),
            data={
                "username": "sherzodergashov",
                "first_name": "Sherzod",
                "last_name": "Ergashov",
                "email": "invalid-email",
                "password": "sher4501"
            }
        )
        user_count = CustomUser.objects.count()

        self.assertEqual(user_count, 0)
        self.assertFormError(response, "form", "email", "Enter a valid email address.")

    def test_unique_username(self):
        # 1
        user = CustomUser.objects.create_user(username="sherzod0101", first_name="Sherzod")
        user.set_password("love74013")
        user.save()

        # 2
        response = self.client.post(
            reverse("users:register"),
            data={
                "username": "sherzod0101",
                "first_name": "Sherzod",
                "last_name": "Ergashov",
                "email": "sher@gmail.com",
                "password": "sher4501"
            }
        )

        # 3
        user_count = CustomUser.objects.count()

        self.assertEqual(user_count, 1)

        # 4
        self.assertFormError(response, "form", "username", "A user with that username already exists.")


class LoginTestCase(TestCase):
    # DRY - dont repeat yourself
    def setUp(self):
        self.user_log = CustomUser.objects.create_user(username="sherzod0101", first_name="Sherzod")
        self.user_log.set_password("love74013")
        self.user_log.save()

    def test_successful_login(self):
        self.client.post(
            reverse("users:login"),
            data={
                "username": "sherzod0101",
                "password": "love74013"
            }
        )
        user = get_user(self.client)
        self.assertTrue(user.is_authenticated)

    def test_wrong_credentials(self):
        self.client.post(
            reverse(
                "users:login"
            ),
            data={
                "username": "wrong-users",
                "password": "love74013"
            }
        )
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)

    def test_error_password(self):
        self.client.post(
            reverse(
                "users:login"
            ),
            data={
                "username": "sherzod0101",
                "password": "loveyou"
            }
        )
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)

    def test_error_user_password(self):
        self.client.post(
            reverse(
                "users:login"
            ),
            data={
                "username": "erroruser",
                "password": "errorpassword"
            }
        )
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)

    def test_logout(self):
        self.client.login(username="sherzod0101", password="love74013")
        self.client.get(reverse("users:logout"))

        user = get_user(self.client)

        self.assertFalse(user.is_authenticated)

class ProfileTestCase(TestCase):
    def test_login_required(self):
        response = self.client.get(reverse("users:profile"))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('users:login') + "?next=/users/profile/")

    def test_profile_details(self):
        user = CustomUser.objects.create_user(
            username="Sherzod740",
            first_name="Sherzod",
            last_name="Ergashov",
            email="sherzodergashov740@gmail.com"
        )
        user.set_password("123456789")
        user.save()

        self.client.login(username="Sherzod740", password="123456789")
        response = self.client.get(reverse("users:profile"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, user.first_name)
        self.assertContains(response, user.last_name)
        self.assertContains(response, user.email)

    def test_update_profile(self):
        user = CustomUser.objects.create_user(
            username="Sherzod740",
            first_name="Sherzod",
            last_name="Ergashov",
            email="sherzodergashov740@gmail.com"
        )
        user.set_password("123456789")
        user.save()

        self.client.login(username="Sherzod740", password="123456789")

        response = self.client.post(
            reverse("users:profile_edit"),
            data={
                "username": "Sherzod740",
                "first_name": "Sherzod",
                "last_name": "Bahodirov",
                "email": "sherzod12345@gmail.com"
            }
        )

        user = CustomUser.objects.get(pk=user.pk)

        self.assertEqual(user.last_name, "Bahodirov")
        self.assertEqual(user.email, "sherzod12345@gmail.com")
        self.assertEqual(response.url, reverse("users:profile"))

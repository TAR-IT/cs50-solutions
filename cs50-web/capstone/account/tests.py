from django.test import TestCase
from django.urls import reverse
from .models import User

class YourAppViewsTest(TestCase):
    def setUp(self):
        # Create a test user using your custom User model
        self.custom_user = User.objects.create(username='testuser', email='test@example.com')
        self.custom_user.set_password('testpassword')
        self.custom_user.save()

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'password',
            'confirmation': 'password',
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 302)  # Check if it redirects after registration

        # Verify that a new user has been created
        new_user = User.objects.get(username='newuser')
        self.assertIsNotNone(new_user)

    def test_register_view_existing_user(self):
        # Attempt to register a user with an existing username
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

        data = {
            'username': 'testuser',
            'email': 'newuser@example.com',
            'password': 'password',
            'confirmation': 'password',
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 200)  # Check if it stays on the registration page

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

        data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, 302)  # Check if it redirects after login

    def test_login_view_invalid_credentials(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

        data = {
            'username': 'testuser',
            'password': 'wrongpassword',
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, 200)  # Check if it stays on the login page

    def test_logout_view(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Check if it redirects after logout

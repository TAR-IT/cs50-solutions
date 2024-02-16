from django.test import TestCase
from django.urls import reverse

from account.models import User

class JourneyViewsTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_journey_view(self):
        response = self.client.get(reverse('journey'))
        self.assertEqual(response.status_code, 200)

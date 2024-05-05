from django.test import TestCase, Client
from unittest.mock import patch
from django.urls import reverse
from .models import User

class UserTestCase(TestCase):
    @patch('api.views.User.objects.values')
    def test_get_users(self, mock_values):
        # Arrange
        mock_values.return_value = [
            {'username': 'user1', 'email': 'user1@example.com'},
            {'username': 'user2', 'email': 'user2@example.com'},
            {'username': 'user3', 'email': 'user3@example.com'},
        ]
        client = Client()

        # Act
        response = client.get(reverse('api:users'))

        # Assert
        self.assertEqual(response.status_code, 200)
        users = response.json()
        self.assertEqual(len(users), 3)
        self.assertEqual(users[0]['username'], 'user1')
        self.assertEqual(users[0]['email'], 'user1@example.com')
        self.assertEqual(users[1]['username'], 'user2')
        self.assertEqual(users[1]['email'], 'user2@example.com')
        self.assertEqual(users[2]['username'], 'user3')
        self.assertEqual(users[2]['email'], 'user3@example.com')
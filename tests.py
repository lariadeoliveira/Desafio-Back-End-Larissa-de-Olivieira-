from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User

class UserAuthTests(APITestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword123'
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_user_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password': 'newpassword123'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login(self):
        response = self.client.post(reverse('login'), {
            'username': self.user_data['username'],
            'password': self.user_data['password']
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_user_balance(self):
        self.client.login(username=self.user_data['username'], password=self.user_data['password'])
        response = self.client.get(reverse('user-balance'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_transfer_funds(self):
        self.client.login(username=self.user_data['username'], password=self.user_data['password'])
        response = self.client.post(reverse('transfer-funds'), {
            'recipient': 'anotheruser',
            'amount': 50
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
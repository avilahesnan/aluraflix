from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.test import override_settings
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class AuthenticationUserTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('aluraflix:Programs-list')
        self.user = User.objects.create_user('teste', password='123')

    def test_authentication_user_credentials(self):
        '''
        Test that verifies a user's authentication with credentials.
        '''

        user = authenticate(username='teste', password='123')

        self.assertTrue((user is not None) and user.is_authenticated)

    @override_settings(CACHE_MIDDLEWARE_SECONDS=0)
    def test_request_get_unauthorized(self):
        '''
        Test that checks for an unauthorized GET request.
        '''

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authentication_username_incorrect(self):
        '''
        Test that verifies authentication with incorrect username.
        '''

        user = authenticate(username='teste1', password='123')

        self.assertFalse((user is not None) and user.is_authenticated)

    def test_authentication_password_incorrect(self):
        '''
        Test that verifies authentication with incorrect password.
        '''

        user = authenticate(username='teste', password='1234')

        self.assertFalse((user is not None) and user.is_authenticated)

    def test_request_get_authorized(self):
        '''
        Test that verifies an authorized GET request.
        '''

        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

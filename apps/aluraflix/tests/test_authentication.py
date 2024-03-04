from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.test import APITestCase


class AuthenticationUserTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user('teste', password='123')

    def test_authentication_user_credentials(self):
        '''
        Test that verifies a user's authentication with credentials.
        '''

        user = authenticate(username='teste', password='123')

        self.assertTrue((user is not None) and user.is_authenticated)

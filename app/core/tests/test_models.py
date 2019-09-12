from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    ''' Make sure the classes in the tests folder inherit from TestCase,
         the methods in them are named test_... like that: '''
    def test_create_user_with_email_succesfull(self):
        email = 'amigo2@hotmail.com'
        password = '123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """test the email for a new user is normalized"""
        email = 'test@AMIGO.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'amigo2@hotmail.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
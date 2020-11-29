from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@gmail.com'
        password = 'pass'
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_with_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@GMAIL.com'
        password = 'pass'
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user without email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email=None, password="abc")

    def test_superuser_is_created_correctly(self):
        """Tests that a superuser is created correctly"""
        user = get_user_model().objects.create_superuser('test@gmail.com', 'test123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

from rest_framework import status
from rest_framework.test import APITestCase


class UserRegisterTest(APITestCase):
    """Testing register user"""

    def test_ez(self):
        self.assertEqual(10, 10, msg="10 was not equal to 10")

    def test_register_correct_user(self):
        """Testing createing a user with correct input"""
        # The correct user input to post
        userBody = {
            "username": "ulrikro",
            "first_name": "Ulrik",
            "last_name": "Roesby",
            "address": "Njords veg 13",
            "password": "password",
            "password2": "password",
            "about_me": "This is some info about me",
            "allergies": [5, 9]
        }
        response = self.client.post('/api/users/register/', userBody)
        expected = status.HTTP_200_OK
        # This is the reponse I have decided to return when a user is succesffully created
        actual = response.status_code
        self.assertEqual(expected, actual,
                         msg="Creating a user returned an unexpected response status for correct input")
        self.assertTrue("token" in response.data,
                        msg="Expected `token` to be in the response data")

    def test_register_user_without_username(self):
        """Testing creating a user without a username"""
        # Body for a user without username
        userBody = {
            "first_name": "Ulrik",
            "last_name": "Roesby",
            "address": "Njords veg 13",
            "password": "password",
            "password2": "password",
            "about_me": "This is some info about me",
            "allergies": [5, 9]
        }
        response = self.client.post('/api/users/register/', userBody)
        expected = status.HTTP_400_BAD_REQUEST
        actual = response.status_code
        self.assertEqual(expected, actual,
                         msg="Creating a user returned an unexpected response")

    def test_register_user_without_first_name(self):
        """Testing creating a user without a first_name"""
        # Body for a user without first_name
        userBody = {
            "username": "ulrikro",
            "last_name": "Roesby",
            "address": "Njords veg 13",
            "password": "password",
            "password2": "password",
            "about_me": "This is some info about me",
            "allergies": [5, 9]
        }
        response = self.client.post('/api/users/register/', userBody)
        expected = status.HTTP_400_BAD_REQUEST
        actual = response.status_code
        self.assertEqual(expected, actual,
                         msg="Creating a user returned an unexpected response")

    def test_register_user_without_last_name(self):
        """Testing creating a user without a last_name"""
        # Body for a user without last_name
        userBody = {
            "username": "ulrikro",
            "first_name": "Ulrik",
            "address": "Njords veg 13",
            "password": "password",
            "password2": "password",
            "about_me": "This is some info about me",
            "allergies": [5, 9]
        }
        response = self.client.post('/api/users/register/', userBody)
        expected = status.HTTP_400_BAD_REQUEST
        actual = response.status_code
        self.assertEqual(expected, actual,
                         msg="Creating a user returned an unexpected response")

    def test_creating_user_without_address(self):
        """Testing creating a user without a address"""
        # Body for a user without address
        userBody = {
            "username": "ulrikro",
            "first_name": "Ulrik",
            "last_name": "Roesby",
            "password": "password",
            "password2": "password",
            "about_me": "This is some info about me",
            "allergies": [5, 9]
        }
        response = self.client.post('/api/users/register/', userBody)
        expected = status.HTTP_400_BAD_REQUEST
        actual = response.status_code
        self.assertEqual(expected, actual,
                         msg="Creating a user returned an unexpected response")

    def test_creating_user_without_password(self):
        """Testing creating a user without a password"""
        # Body for a user without password
        userBody = {
            "username": "ulrikro",
            "first_name": "Ulrik",
            "last_name": "Roesby",
            "address": "Njords veg 13",
            "password2": "password",
            "about_me": "This is some info about me",
            "allergies": [5, 9]
        }
        response = self.client.post('/api/users/register/', userBody)
        expected = status.HTTP_400_BAD_REQUEST
        # This is the reponse I have decided to return when a user is succesffully created
        actual = response.status_code
        self.assertEqual(expected, actual,
                         msg="Creating a user returned an unexpected response")

    def test_creating_user_without_password2(self):
        """Testing creating a user without a password2"""
        # Body for a user without password2
        userBody = {
            "username": "ulrikro",
            "first_name": "Ulrik",
            "last_name": "Roesby",
            "address": "Njords veg 13",
            "password": "password",
            "about_me": "This is some info about me",
            "allergies": [5, 9]
        }
        response = self.client.post('/api/users/register/', userBody)
        expected = status.HTTP_400_BAD_REQUEST
        # This is the reponse I have decided to return when a user is succesffully created
        actual = response.status_code
        self.assertEqual(expected, actual,
                         msg="Creating a user returned an unexpected response")

    def test_creating_user_without_about_me(self):
        """Testing creating a user without a about_me, should work"""
        # Body for a user without about_me
        userBody = {
            "username": "ulrikro",
            "first_name": "Ulrik",
            "last_name": "Roesby",
            "address": "Njords veg 13",
            "password": "password",
            "password2": "password",
            "allergies": [5, 9]
        }
        response = self.client.post('/api/users/register/', userBody)
        expected = status.HTTP_200_OK
        # This is the reponse I have decided to return when a user is succesffully created
        actual = response.status_code
        self.assertEqual(expected, actual,
                         msg="Creating a user returned an unexpected response")

    def test_creating_user_without_allergies(self):
        """Testing creating a user without allergies:  should work"""
        # Body for a user without allergies
        userBody = {
            "username": "ulrikro",
            "first_name": "Ulrik",
            "last_name": "Roesby",
            "address": "Njords veg 13",
            "password": "password",
            "password2": "password",
        }
        response = self.client.post('/api/users/register/', userBody)
        expected = status.HTTP_200_OK
        actual = response.status_code
        self.assertEqual(expected, actual,
                         msg="Creating a user returned an unexpected response")

    def test_creating_user_passwords_dont_match(self):
        """Testing creating a user without matching passwords"""
        # Body for a user without matching passwords
        userBody = {
            "username": "ulrikro",
            "first_name": "Ulrik",
            "last_name": "Roesby",
            "address": "Njords veg 13",
            "password": "password",
            "password2": "password2",
            "allergies": [5, 9]
        }
        response = self.client.post('/api/users/register/', userBody)
        expected = status.HTTP_400_BAD_REQUEST
        # This is the reponse I have decided to return when a user is succesffully created
        actual = response.status_code
        self.assertEqual(expected, actual,
                         msg="Creating a user returned an unexpected response")

from unittest.case import skip

from dine_backend.tests.constants import DINNER_1, DINNER_2, USER_1, USER_2
from django.conf import UserSettingsHolder
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class EditDinnerTest(APITestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        client = APIClient()
        # Creating a user
        user_response = client.post("/api/users/register/", USER_1)
        cls.userToken = user_response.data["token"]
        client = APIClient()
        client.defaults['HTTP_AUTHORIZATION'] = "Token " + cls.userToken
        response = client.post("/api/dinners/", DINNER_1)
        assert response.status_code == status.HTTP_201_CREATED
        super().setUpTestData()

    def setUp(self):
        """Setting the client up to use the token header"""
        self.client.defaults['HTTP_AUTHORIZATION'] = "Token " + self.userToken

    def test_edit_correct_dish(self):
        """Test that a correct request editing the dish works"""
        changeDinner = {
            'dish': 'Carbonara med bacon'
        }
        # Changing the dinner
        put_response = self.client.patch('/api/dinners/1/', changeDinner)
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)

        # Check that the changes have taken effect:
        # Creating a deep dopy of DINNER_1
        expected = {}
        for key in DINNER_1:
            expected[key] = DINNER_1[key]
        expected['dish'] = changeDinner['dish']
        get_response = self.client.get('/api/dinners/1/')
        self.assertEqual(expected, get_response.data,
                         msg="The data was not changed as expected")

    def test_edit_correct_cuisine(self):
        """Test that a correct request editing the cuisine works"""
        changeDinner = {
            'cuisine': 'Annet'
        }
        # Changing the dinner
        put_response = self.client.patch('/api/dinners/1/', changeDinner)
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)

        # Check that the changes have taken effect:
        # Creating a deep dopy of DINNER_1
        expected = {}
        for key in DINNER_1:
            expected[key] = DINNER_1[key]
        expected['cuisine'] = changeDinner['cuisine']
        get_response = self.client.get('/api/dinners/1/')
        self.assertEqual(expected, get_response.data,
                         msg="The data was not changed as expected")

    def test_edit_correct_date(self):
        """Test that a correct request editing the date works"""
        changeDinner = {
            'date': '2021-05-17T16:00:00Z'
        }
        # Changing the dinner
        put_response = self.client.patch('/api/dinners/1/', changeDinner)
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)

        # Check that the changes have taken effect:
        # Creating a deep dopy of DINNER_1
        expected = {}
        for key in DINNER_1:
            expected[key] = DINNER_1[key]
        expected['date'] = changeDinner['date']
        get_response = self.client.get('/api/dinners/1/')
        self.assertEqual(expected, get_response.data,
                         msg="The data was not changed as expected")

    def test_edit_incorrect_date(self):
        """Test that a correct request editing the date works"""
        changeDinner = {
            'date': '2021.11'
        }
        # Changing the dinner
        put_response = self.client.patch('/api/dinners/1/', changeDinner)
        self.assertEqual(put_response.status_code, status.HTTP_400_BAD_REQUEST)

        # Check that the changes have taken effect:
        # Creating a deep dopy of DINNER_1
        expected = {}
        for key in DINNER_1:
            expected[key] = DINNER_1[key]
        expected['date'] = changeDinner['date']
        get_response = self.client.get('/api/dinners/1/')
        self.assertNotEqual(expected, get_response.data,
                            msg="The data was changed, which was not expected")

    def test_edit_correct_location(self):
        """Test that a correct request editing the location works"""
        changeDinner = {
            'location': 'Galdhøpiggen'
        }
        # Changing the dinner
        put_response = self.client.patch('/api/dinners/1/', changeDinner)
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)

        # Check that the changes have taken effect:
        # Creating a deep dopy of DINNER_1
        expected = {}
        for key in DINNER_1:
            expected[key] = DINNER_1[key]
        expected['location'] = changeDinner['location']
        get_response = self.client.get('/api/dinners/1/')
        self.assertEqual(expected, get_response.data,
                         msg="The data was not changed as expected")

    def test_edit_correct_description(self):
        """Test that a correct request editing the description works"""
        changeDinner = {
            'description': 'Dette er en fin middag'
        }
        # Changing the dinner
        put_response = self.client.patch('/api/dinners/1/', changeDinner)
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)

        # Check that the changes have taken effect:
        # Creating a deep dopy of DINNER_1
        expected = {}
        for key in DINNER_1:
            expected[key] = DINNER_1[key]
        expected['description'] = changeDinner['description']
        get_response = self.client.get('/api/dinners/1/')
        self.assertEqual(expected, get_response.data,
                         msg="The data was not changed as expected")

    def test_edit_correct_allergies(self):
        """Test that a correct request editing the allergies works"""
        changeDinner = {
            'allergies': [1, 2, 3]
        }
        # Changing the dinner
        put_response = self.client.patch('/api/dinners/1/', changeDinner)
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)

        # Check that the changes have taken effect:
        # Creating a deep dopy of DINNER_1
        expected = {}
        for key in DINNER_1:
            expected[key] = DINNER_1[key]
        expected['allergies'] = changeDinner['allergies']
        get_response = self.client.get('/api/dinners/1/')
        self.assertEqual(expected, get_response.data,
                         msg="The data was not changed as expected")

    def test_edit_incorrect_allergies(self):
        """Test that a incorrect request editing the allergies does not work"""
        changeDinner = {
            'allergies': "En streng går ikke"
        }
        # Changing the dinner
        put_response = self.client.put('/api/dinners/1/', changeDinner)
        self.assertEqual(put_response.status_code, status.HTTP_400_BAD_REQUEST)

        # Check that the changes have not taken effect:
        # Creating a deep dopy of DINNER_1
        expected = {}
        for key in DINNER_1:
            expected[key] = DINNER_1[key]
        expected['allergies'] = changeDinner['allergies']
        get_response = self.client.get('/api/dinners/1/')
        self.assertNotEqual(expected, get_response.data,
                            msg="The data was changed, which was not expected")

    def test_edit_owner_should_not_work(self):
        """Testing that an attempt to edit owner does not work"""
        changeDinner = {
            'owner': 2
        }
        # Changing the dinner
        put_response = self.client.patch('/api/dinners/1/', changeDinner)
        self.assertEqual(put_response.status_code, status.HTTP_400_BAD_REQUEST)

        # Check that the changes have not taken effect:
        # Creating a deep dopy of DINNER_1
        expected = {}
        for key in DINNER_1:
            expected[key] = DINNER_1[key]
        expected['owner'] = changeDinner['owner']
        get_response = self.client.get('/api/dinners/1/')
        self.assertNotEqual(expected, get_response.data,
                            msg="The data was changed, which was not expected")

    def test_edit_signedupusers_should_not_work(self):
        """Testing that an attempt to edit signed_up_users does not work"""
        changeDinner = {
            'signed_up_users': [2, 3]
        }
        # Changing the dinner
        put_response = self.client.put('/api/dinners/1/', changeDinner)
        self.assertEqual(put_response.status_code, status.HTTP_400_BAD_REQUEST)

        # Check that the changes have not taken effect:
        # Creating a deep dopy of DINNER_1
        expected = {}
        for key in DINNER_1:
            expected[key] = DINNER_1[key]
        expected['signed_up_users'] = changeDinner['signed_up_users']
        get_response = self.client.get('/api/dinners/1/')
        self.assertNotEqual(expected, get_response.data,
                            msg="The data was changed, which was not expected")

    def test_edit_id_should_not_work(self):
        """Testing that an attempt to edit id does not work"""
        # Posting a dinner
        changeDinner = {
            'id': 4
        }
        # Changing the dinner
        put_response = self.client.patch('/api/dinners/1/', changeDinner)
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)

        # Check that the changes have not taken effect:
        # Creating a deep dopy of DINNER_1
        expected = {}
        for key in DINNER_1:
            expected[key] = DINNER_1[key]
        expected['id'] = changeDinner['id']
        get_response = self.client.get('/api/dinners/4/')
        self.assertEqual(get_response.status_code, status.HTTP_404_NOT_FOUND)
        get_dinner = self.client.get('/api/dinners/1/')
        self.assertEqual(DINNER_1, get_dinner.data,
                         msg="The recieved dinner after editing id was not as expected")

    def test_edit_iscanceled_should_work(self):
        """Testing that an attempt to edit is_canceled field should work"""
        changeDinner = {
            'is_canceled': True
        }
        # Changing the dinner
        put_response = self.client.patch('/api/dinners/1/', changeDinner)
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)

        # Check that the changes have not taken effect:
        # Creating a deep dopy of DINNER_1
        expected = {}
        for key in DINNER_1:
            expected[key] = DINNER_1[key]
        expected['is_canceled'] = changeDinner['is_canceled']
        get_response = self.client.get('/api/dinners/4/')
        self.assertEqual(get_response.status_code, status.HTTP_404_NOT_FOUND)

    def test_cannot_edit_dinner_if_users_is_not_owner(self):
        """Test that you cannot edit a dinner if you are not the owner"""
        # Resetting the defaults of the client
        self.client.defaults['HTTP_AUTHORIZATION'] = ""
        # Creating a new user and post a dinner with this user
        user_response = self.client.post('/api/users/register/', USER_2)
        # This user will have id 2
        self.assertEqual(user_response.status_code,
                         status.HTTP_200_OK, msg="Failed to create new user")
        user2Token = user_response.data['token']
        # Posting a dinner for the new user
        self.client.defaults['HTTP_AUTHORIZATION'] = f"Token {user2Token}"
        response = self.client.post(
            "/api/dinners/", DINNER_2)
        # This dinner will have id 2
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # A changeDinner dict that should work
        changeDinner = {
            'dish': 'A new dish: superfish'
        }
        # Trying to change that dinner that has another user
        self.client.defaults['HTTP_AUTHORIZATION'] = f"Token {self.userToken}"
        patch_response = self.client.patch('/api/dinners/2/', changeDinner)
        self.assertEqual(patch_response.status_code,
                         status.HTTP_403_FORBIDDEN)

        # Check that the changes have not taken effect:
        # Creating a deep dopy of DINNER_2
        expected = {}
        for key in DINNER_2:
            expected[key] = DINNER_1[key]
        expected['dish'] = changeDinner['dish']
        get_response = self.client.get('/api/dinners/2/')
        self.assertNotEqual(expected, get_response.data,
                            msg="The data was changed, which was not expected")

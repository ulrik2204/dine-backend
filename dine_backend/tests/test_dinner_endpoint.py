import json

from dine_backend.tests.constants import USER_1
from django.http.request import QueryDict
from rest_framework import status
from rest_framework.test import APIClient, APITestCase, force_authenticate


class DinnerPostTest(APITestCase):
    """Testing the /api/dinners/ endpoints"""

    @classmethod
    def setUpTestData(cls):
        """Create a user and get a token to post the dinners with"""
        client = APIClient()
        # Creating the user
        response = client.post("/api/users/register/", USER_1)
        cls.userToken = response.data["token"]
        super().setUpTestData()

    def setUp(self):
        """Setting the client up to use the token header"""
        self.client.defaults['HTTP_AUTHORIZATION'] = 'Token ' + self.userToken

    def test_post_correct_dinner(self):
        """Test posting a correct dinner to the API"""
        testDinner = {
            "dish": "Lasagne",
            "cuisine": "Italiensk",
            "date": "2021-04-19T11:11",
            "location": "Oslo",
            "allergies": [2, 6]
        }
        # self.client.credentials(HTTP_AUTHORIZATION="Token " + self.userToken)
        response = self.client.post(
            '/api/dinners/', testDinner
        )
        # The status code should be 201
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_dinner_without_dish(self):
        """Testing sending adinner without dish"""
        testDinner = {
            "cuisine": "Italiensk",
            "date": "2021-04-19T11:11",
            "location": "Oslo",
            "allergies": [2, 6]
        }
        # self.client.credentials(HTTP_AUTHORIZATION="Token " + self.userToken)
        response = self.client.post(
            '/api/dinners/', testDinner
        )
        # The status code should be 400
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_dinner_without_cuisine(self):
        """Testing sending adinner without cuisine"""
        testDinner = {
            "dish": "Lasagne",
            "date": "2021-04-19T11:11",
            "location": "Oslo",
            "allergies": [2, 6]
        }
        # self.client.credentials(HTTP_AUTHORIZATION="Token " + self.userToken)
        response = self.client.post(
            '/api/dinners/', testDinner
        )
        # The status code should be 400
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_dinner_without_date(self):
        """Testing sending adinner without date"""
        testDinner = {
            "dish": "Lasagne",
            "cuisine": "Italiensk",
            "location": "Oslo",
            "allergies": [2, 6]
        }
        # self.client.credentials(HTTP_AUTHORIZATION="Token " + self.userToken)
        response = self.client.post(
            '/api/dinners/', testDinner
        )
        # The status code should be 400
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_dinner_without_allergies(self):
        """Testing sending adinner without allergies"""
        testDinner = {
            "dish": "Lasagne",
            "cuisine": "Italiensk",
            "date": "2021-04-19T11:11",
        }
        # self.client.credentials(HTTP_AUTHORIZATION="Token " + self.userToken)
        response = self.client.post(
            '/api/dinners/', testDinner
        )
        # The status code should be 201
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_dinner_with_owner(self):
        """Testing sending a dinner with owner does not affect the owner of the dish"""
        testDinner = {
            "dish": "Lasagne2",
            "cuisine": "Italiensk",
            "date": "2021-04-19T11:11",
            "owner": 100,
            "location": "Oslo",
            "allergies": [2, 6]
        }
        # self.client.credentials(HTTP_AUTHORIZATION="Token " + self.userToken)
        response = self.client.post(
            '/api/dinners/', testDinner
        )
        # The status code should be 201
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check that all dinners created now have owner 1
        all1 = True
        dinners_response = APIClient().get('/api/dinners/')
        json_resp = dinners_response.json()
        for dinner in json_resp:
            if dinner['owner'] != 1:
                all1 = False
                break
        self.assertTrue(
            all1, msg="The owner set when specifying the owner was not the user")

    def test_post_dinner_without_location(self):
        """Testing sending adinner without location"""
        testDinner = {
            "dish": "Lasagne",
            "cuisine": "Italiensk",
            "location": "Oslo",
            "allergies": [2, 6]
        }
        # self.client.credentials(HTTP_AUTHORIZATION="Token " + self.userToken)
        response = self.client.post(
            '/api/dinners/', testDinner
        )
        # The status code should be 400
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_dinner_when_not_logged_in(self):
        """Testing sending a dinner without location"""
        testDinner = {
            "dish": "Spaghetti",
            "cuisine": "Italiensk",
            "date": "2021-04-19T11:11",
            "location": "Oslo",
            "allergies": [2, 6]
        }
        # self.client.credentials(HTTP_AUTHORIZATION="Token " + self.userToken)
        self.client.defaults['HTTP_AUTHORIZATION'] = ""
        response = self.client.post(
            '/api/dinners/', testDinner
        )
        # The status code should be 401 unauthorized
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

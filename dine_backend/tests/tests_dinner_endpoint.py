from django.http import response
from dine_backend.tests.constants import DINNER_1, DINNER_2, USER_1
from django.test import TestCase
from django.test import Client


class DinnerTest(TestCase):

    def __init__(self, methodName: str) -> None:
        """Log in user and post some data"""
        super().__init__(methodName)
        c = Client()
        response = c.post('/api/users/register/', USER_1)
        headers = {'Content-Type': 'application/json',
        'Authorization': 'Token ' + response.data['token']}
        self.c = Client(headers)
        self.c.post('/api/dinners/', DINNER_1)
        self.c.post('/api/dinners/', DINNER_2)



        
        


    def test_get_all_dinners(self):
        response = self.c.get('/api/dinners/')
        expected = [DINNER_1, DINNER_2]
        
        

USER_1 = {
    "username": "test_user",
    "first_name": "Ola",
    "last_name": "Nordmann",
    "address": "EnAdresse",
    "password": "password",
    "password2": "password",
    "allergies": [5, 9]
}

USER_2 = {
    "username": "test_user2",
    "first_name": "Noen",
    "last_name": "Noensen",
    "address": "Heisannveien",
    "password": "password",
    "password2": "password",
    "allergies": [1, 2, 3]
}


DINNER_1 = {
    "id": 1,
    "dish": "Carbonara amazing",
    "cuisine": "Italiensk",
    "date": "2021-04-19T11:11:00Z",
    "location": "Oslo",
    "owner": 1,  # The owner that will be assigned
    "description": "Dette er en beskrivelse",
    "allergies": [2, 6],
    "signed_up_users": [],  # Has to be empty, the request does not care about this one
    "is_canceled": False
}

DINNER_2 = {
    "id": 2,
    "dish": "Spaghetti bolognese",
    "cuisine": "Italiensk",
    "date": "2021-04-19T11:11:00Z",
    "location": "Oslo",
    "owner": 1,  # The owner that will be assigned
    "description": "",
    "allergies": [5],
    "signed_up_users": [],  # Has to be empty, the request does not care about this one
    "is_canceled": False
}

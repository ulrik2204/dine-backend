from django.test import TestCase


class TestTemplate(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_somethnin(self):
        actual = 10
        expected = 10
        self.assertEqual(actual, expected)

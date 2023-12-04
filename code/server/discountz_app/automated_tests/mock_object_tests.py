from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from unittest.mock import patch
from discountz_app.models import Student, Discount


class CustomLoginViewTest(TestCase):
    """
    Test suite for the CustomLoginView.

    This class tests the functionality of the CustomLoginView,
    particularly focusing on user authentication and token generation.
    """

    def setUp(self):
        """
        Set up the test environment before each test.

        Initializes an APIClient and creates a test user in the database.
        """

        self.client = APIClient()
        self.student = Student.objects.create_user(
            "sam.altman@nau.edu", "x12sad84Cxadlew"
        )

    @patch("rest_framework.authtoken.models.Token.objects.get_or_create")
    def test_login_response(self, mock_get_or_create):
        """
        Test the login response of CustomLoginView.

        Ensures that a successful login returns the correct HTTP status and token.
        """
        mock_token = Token(key="testtoken123")
        mock_get_or_create.return_value = (mock_token, True)

        response = self.client.post(
            "/api/login/",
            {"username": "sam.altman@nau.edu", "password": "x12sad84Cxadlew"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["token"], "testtoken123")


class RegisterViewTest(TestCase):
    """
    Test suite for the register_view.

    This class tests the user registration functionality, ensuring that
    new users are correctly registered and appropriate responses are returned.
    """

    def setUp(self):
        """
        Set up the test environment before each test.

        Initializes an APIClient to be used for making requests in the tests.
        """
        self.client = APIClient()

    @patch("discountz_app.views.CustomRegisterSerializer")
    def test_register_user(self, mock_serializer):
        """
        Test the user registration process.

        Ensures that a new user can be successfully registered and that the
        response contains the correct HTTP status and user data.
        """
        mock_serializer().is_valid.return_value = True
        mock_serializer().data = {
            "email": "jamie.polymer@asu.edu",
            "first_name": "Jamie",
            "last_name": "Polymer",
        }

        response = self.client.post(
            "/api/register/",
            {
                "email": "jamie.polymer@asu.edu",
                "first_name": "Jamie",
                "last_name": "Polymer",
                "password": "cs386-2023-Rox",
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["user"]["email"], "jamie.polymer@asu.edu")

from django.test import TestCase
from ..models import Notification, Student
import datetime

class NotificationModelTest(TestCase):
    """
    Tests for the Notification model. This ensures that each aspect of the model functions as expected.
    These tests now use a fictional student named Peter Parker for test data.
    """

    def setUp(self):
        """
        Set up data for testing the Notification model. This method is run before each test.
        """
        # Create a student named Peter Parker for associating notifications
        self.student_peter = Student.objects.create(
            first_name="Peter",
            last_name="Parker",
            email="peter@notspiderman.edu"
        )

        # Create a notification for the student with a specific message
        self.notification = Notification.objects.create(
            student=self.student_peter,
            message="You have new student discounts available!"
        )

    def test_notification_creation_with_valid_data(self):
        """
        Test the successful creation of a notification instance with valid data.
        """
        self.assertEqual(self.notification.student, self.student_peter)
        self.assertEqual(self.notification.message, "You have new student discounts available!")
        self.assertFalse(self.notification.is_read)
        self.assertIsInstance(self.notification.date_created, datetime.datetime)

    def test_mark_as_read_method(self):
        """
        Test the mark_as_read method of the Notification model.
        This method should change the is_read status of the notification to True.
        """
        self.assertFalse(self.notification.is_read)
        self.notification.mark_as_read()
        self.assertTrue(self.notification.is_read)

    def test_notification_string_representation(self):
        """
        Test the __str__ method of the Notification model.
        This method should return a string representation of the notification, including the student username and a snippet of the message.
        """
        expected_str = f"Notification for {self.student_peter.username}: You have new stud..."
        self.assertEqual(str(self.notification), expected_str)


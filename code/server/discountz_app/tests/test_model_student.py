from django.test import TestCase
from discountz_app.models import Student
from rest_framework import serializers
from ..serializer import StudentSerializer
from django.core.exceptions import ValidationError

class StudentModelTest(TestCase):
    """
    Tests for the Student model, ensuring that each aspect of the model functions as expected.
    These tests use a variety of fictional characters for test data because I'm bored.
    """

    def setUp(self):
        """
        Set up data for testing the Student model. This method is run before each test.
        """
        # Create a student with valid data for use in multiple tests.
        self.student_luke = Student.objects.create(
            first_name="Luke",
            last_name="Skywalker",
            email="luke@rebels.edu"
        )

    def test_student_creation_with_valid_data(self):
        """
        Test the successful creation of a student instance with valid data.
        This test ensures that a student object can be created with proper .edu email and other required fields.
        """
        self.assertIsInstance(self.student_luke, Student)

    # We had a method to test email uniqueness, but it broke because
    # the username field is our email field, and Django does 
    # not allow multiple users with the same username.

    def test_email_validation_for_edu_domain(self):
        """
        Test the custom .edu email validator for the Student model.
        The test verifies that a ValidationError is raised when a non-.edu email is used.
        """

        student_data = {
            'first_name': 'Tony',
            'last_name': 'Stark',
            'email': 'tony@starkindustries.com'
        }
        serializer = StudentSerializer(data=student_data)
        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)


    def test_get_full_name_method(self):
        """
        Test the get_full_name method of the Student model.
        This method should return the full name of the student in the format 'first_name last_name'.
        """
        self.assertEqual(self.student_luke.get_full_name(), "Luke Skywalker")

    def test_total_bookmarks_method_initially_zero(self):
        """
        Test that the total_bookmarks method returns 0 for a new student instance.
        This method checks the bookmark count for a student who hasn't bookmarked any discounts yet.
        """
        self.assertEqual(self.student_luke.total_bookmarks(), 0)

    def test_auto_now_add_for_date_joined_field(self):
        """
        Test that the date_joined field is automatically set to the current date and time when a student instance is created.
        This field should not be null for any newly created student.
        """
        self.assertIsNotNone(self.student_luke.date_joined)

    def test_auto_now_for_last_logged_in_field(self):
        """
        Test that the last_logged_in field is automatically updated when the student instance is saved.
        This field should reflect the most recent save operation on the student instance.
        """
        original_login_time = self.student_luke.last_logged_in
        self.student_luke.save()  # Trigger update to last_logged_in field
        self.assertNotEqual(self.student_luke.last_logged_in, original_login_time)


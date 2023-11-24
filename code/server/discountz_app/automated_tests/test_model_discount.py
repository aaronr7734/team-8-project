from django.test import TestCase
from discountz_app.models import Discount, Student, Category
from django.utils import timezone
import datetime


class DiscountModelTest(TestCase):
    """
    Tests for the Discount model, ensuring that each attribute and method functions correctly.
    These tests use a variety of fictional business names and discount details for test data.
    """

    def setUp(self):
        """
        Set up data for testing the Discount model.
        This involves creating a dummy student and categories for associating with discounts.
        """
        self.student_hermione = Student.objects.create(
            first_name="Hermione", last_name="Granger", email="hermione@hogwarts.edu"
        )

        self.category_magic = Category.objects.create(name="Magic Supplies")
        self.category_potions = Category.objects.create(name="Potions")

        self.discount_wands = Discount.objects.create(
            name="Wizard's Wand Discount",
            description="10% off on all wands",
            business_name="Ollivanders",
            url="https://www.ollivanders.co.uk",
            location="Diagon Alley",
            date_added=timezone.now(),
            added_by=self.student_hermione,
        )
        self.discount_wands.categories.set([self.category_magic])

    def test_discount_creation(self):
        """
        Test the creation of a Discount instance with valid data.
        """
        self.assertIsInstance(self.discount_wands, Discount)

    def test_discount_string_representation(self):
        """
        Test the string representation of a Discount instance.
        """
        self.assertEqual(
            str(self.discount_wands), "Ollivanders: Wizard's Wand Discount"
        )

    def test_discount_categories_association(self):
        """
        Test the association of categories with a Discount instance.
        """
        self.assertIn(self.category_magic, self.discount_wands.categories.all())

    def test_discount_auto_now_add_date_added(self):
        """
        Test that the date_added field is automatically set upon creation of a discount instance.
        """
        self.assertEqual(self.discount_wands.date_added.date(), datetime.date.today())

    def test_get_students_who_bookmarked_empty_initially(self):
        """
        Test that the get_students_who_bookmarked method returns an empty QuerySet initially.
        """
        self.assertFalse(self.discount_wands.get_students_who_bookmarked().exists())

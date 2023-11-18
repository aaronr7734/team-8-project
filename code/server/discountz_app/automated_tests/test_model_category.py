from django.test import TestCase
from ..models import Category, Discount  

class CategoryModelTest(TestCase):
    """
    Tests for the Category model. This ensures that each aspect of the model functions as expected.
    These tests use fictional discounts for test data.
    """

    def setUp(self):
        """
        Set up data for testing the Category model. This method is run before each test.
        """
        #Create categories with valid names
        self.category_food = Category.objects.create(name="Food")
        self.category_tech = Category.objects.create(name="Technology")

        #Create some fictional discounts and assign them to categories
        Discount.objects.create(name="Pizza Discount", category=self.category_food)
        Discount.objects.create(name="Laptop Discount", category=self.category_tech)

    def test_category_creation_with_valid_name(self):
        """
        Test the successful creation of a category instance with a valid name.
        """
        self.assertEqual(self.category_food.name, "Food")
        self.assertEqual(self.category_tech.name, "Technology")

    def test_get_discounts_in_category_method(self):
        """
        Test the get_discounts_in_category method of the Category model.
        This method should return all discounts associated with a specific category.
        """
        food_discounts = self.category_food.get_discounts_in_category()
        tech_discounts = self.category_tech.get_discounts_in_category()

        self.assertEqual(food_discounts.count(), 1)
        self.assertEqual(tech_discounts.count(), 1)
        self.assertEqual(food_discounts.first().name, "Pizza Discount")
        self.assertEqual(tech_discounts.first().name, "Laptop Discount")

    def test_category_string_representation(self):
        """
        Test the __str__ method of the Category model.
        This method should return the name of the category.
        """
        self.assertEqual(str(self.category_food), "Food")
        self.assertEqual(str(self.category_tech), "Technology")

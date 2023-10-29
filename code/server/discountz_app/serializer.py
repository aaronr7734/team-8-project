"""
serializers.py

This module contains serializers for the Discountz app. Serializers allow complex data types
such as queryset and model instances to be converted to Python data types that can be rendered
into JSON, XML, or other content types.
"""
from rest_framework import serializers
from .models import Student, Discount, Category, Notification

class StudentSerializer(serializers.ModelSerializer):
    """
    Student Serializer
    
    This serializer converts the Student model into JSON format for API interactions.
    
    Attributes:
        model (Model): The model the serializer is based on, in this case, Student.
        fields (list): The fields from the Student model that will be serialized.
    """
    
    class Meta:
        model = Student
        fields = ["id", "first_name", "last_name", "email", "date_joined", "last_logged_in"]

    def create(self, validated_data):
        """
        Override the default create method to populate the username field with the email address.
        
        Parameters:
            validated_data (dict): The validated data from the incoming request.
        Returns:
            Student: The newly created Student object.
        """
        # Set the username field to the email address
        validated_data['username'] = validated_data['email']
        return Student.objects.create(**validated_data)

class CustomRegisterSerializer(serializers.ModelSerializer):
    """
    Custom Register Serializer

    This serializer extends the default ModelSerializer to use the custom Student model.
    It automatically maps the email, first_name, last_name, and password fields.

    Attributes:
        None (inherits all attributes from ModelSerializer)
    """
    
    class Meta:
        """
        Meta Class
        
        Specifies the model to use and the fields to be serialized.
        """
        model = Student  # Use Student instead of the default User
        fields = ('email', 'first_name', 'last_name', 'password')
        
    def create(self, validated_data):
        """
        Create Method

        Overrides the default create method to use Student's create_user method.

        Parameters:
            validated_data (dict): The validated data from the incoming request.

        Returns:
            Student: The newly created Student object.
        """
        user = Student.objects.create_user(  # Use Student.objects
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
        )
        return user

class DiscountSerializer(serializers.ModelSerializer):
    """
    Discount Serializer
    
    This serializer converts the Discount model into JSON format for API interactions.
    
    Attributes:
        model (Model): The model the serializer is based on, in this case, Discount.
        fields (list): The fields from the Discount model that will be serialized.
    """
    
    class Meta:
        model = Discount
        fields = ["id", "name", "description", "business_name", "url", "location", "date_added"]

class CategorySerializer(serializers.ModelSerializer):
    """
    Category Serializer
    
    This serializer converts the Category model into JSON format for API interactions.
    
    Attributes:
        model (Model): The model the serializer is based on, in this case, Category.
        fields (list): The fields from the Category model that will be serialized.
    """
    
    class Meta:
        model = Category
        fields = ["id", "name"]

class NotificationSerializer(serializers.ModelSerializer):
    """
    Notification Serializer
    
    Converts the Notification model into JSON format for API interactions.
    
    Attributes:
        model (Model): The model the serializer is based on, in this case, Notification.
        fields (list): The fields from the Notification model that will be serialized.
    """
    
    class Meta:
        model = Notification
        fields = ['id', 'message', 'date_created', 'is_read']
from django.core.exceptions import ValidationError
"""
validator.py

This module contains custom validators for the discountz app.
More will be added as time permits.
"""

def validate_edu_email(email_address):
    """
    Validates that the provided email address ends in .edu.

    args:
        email_address (str): The email address to validate.

    Raises:
        ValidationError: If the email address does not end in .edu.
    
    Returns:
        None: if validation succeeds, nothing is returned.
        Exception is raised otherwise.
    """
    if not email_address.endswith('.edu'):
        raise ValidationError('Email address must end in .edu')

def validate_only_letters(value):
    """
    Validates that the provided string contains only letters.

    args:
        value (str): The string to validate.

    Raises:
        ValidationError: If the string contains anything other than letters.
    
    Returns:
        None: if validation succeeds, nothing is returned.
        Exception is raised otherwise.
    """
    if not value.isalpha():
        raise ValidationError('String must contain only letters')


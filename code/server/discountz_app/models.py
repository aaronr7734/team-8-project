"""
models.py

This module defines the data models for the discountz app.
Here you'll find classes that interact with the database,
structuring the way the data is stored and retrieved.
"""

from django.core.validators import EmailValidator
from django.contrib.auth.models import (
    AbstractUser,
    Group,
    Permission,
    UserManager as DefaultUserManager,
)
from . import validator

from django.db import models


class StudentManager(DefaultUserManager):
    """
    Custom manager for Student model.
    """

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        extra_fields.setdefault("username", email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("username", email)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class Student(AbstractUser):
    """
    This model inherits attributes like 'first_name', 'last_name', 'username' and 'password' from Django's AbstractUser.

    Attributes:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        email (str): The student's .edu email address.
        date_joined (datetime): Date when student joined the platform.
        last_logged_in (datetime): Date when student last logged in.
        bookmarks (ManyToMany): Many-to-many relationship with the Discount model.
        is_superuser (bool): Determines whether the student is a superuser or not.
        groups (ManyToMany): Specifies the many-to-many relationship
        between the Student and Group models, representing group affiliations for the student.
        user_permissions (ManyToMany): Specifies the many-to-many relationship
        between the Student and Permission models, representing individual permissions granted
        to the student.
    """

    email = models.EmailField(
        validators=[EmailValidator(), validator.validate_edu_email], unique=True
    )
    date_joined = models.DateTimeField(auto_now_add=True)
    last_logged_in = models.DateTimeField(auto_now=True)
    bookmarks = models.ManyToManyField("Discount", related_name="bookmarked_by")
    is_superuser = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        Group,
        verbose_name="groups",
        blank=True,
        related_name="student_groups",  # Custom related_name here
        related_query_name="student",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="user permissions",
        blank=True,
        related_name="student_user_permissions",  # Custom related_name here
        related_query_name="student",
    )

    objects = StudentManager()

    def get_full_name(self):
        """
        Returns the student's full name.

        Returns:
            str: The student's full name.
        """
        return f"{self.first_name} {self.last_name}"

    def total_bookmarks(self):
        """
        Count and return the total number of bookmarks associated with this student.

        Returns:
            int: Count of bookmarks linked to this student instance.
        """
        return self.bookmarks.count()

    def __str__(self):
        return self.get_full_name()


class Discount(models.Model):
    """
    Discount model

    Attributes:
        name (CharField): The name of the discount.
        description (TextField): A description of, you guessed it, the discount.
        business_name (CharField): The name of the business offering the discount.
        url (URLField): The URL students can click to redeem the discount.
        location (CharField): The location where the discount can be redeemed (if applicable.)
        categories (ManyToMany): The categories the discount belongs to.
        date_added (DateTime) The date the discount was added to the platform.
        added_by: (ForeignKey) The admin who added the discount.
    """

    name = models.CharField(max_length=150)
    description = models.TextField()
    business_name = models.CharField(max_length=150)
    url = models.URLField()
    location = models.CharField(max_length=150)
    categories = models.ManyToManyField("Category", related_name="discounts")
    date_added = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(
        Student, on_delete=models.SET_NULL, null=True, blank=True
    )

    def get_students_who_bookmarked(self):
        """
        Returns a QuerySet of all students who've bookmarked this discount.

        Returns:
            QuerySet: Students who've bookmarked the discount.
        """
        return self.bookmarked_by.all()

    def __str__(self):
        return f"{self.business_name}: {self.name}"


class Category(models.Model):
    """
    Category model

    Attributes:
        name (charField): The name of the category.
    """

    name = models.CharField(max_length=150)

    def get_discounts_in_category(self):
        """
        Returns a QuerySet of all discount objects associated with this category.

        Returns:
            QuerySet: A QuerySet containing all Discount objects that belong to this category.
        """
        return self.discounts.all()

    def __str__(self):
        return self.name


class Notification(models.Model):
    """
    Notification model

    Attributes:
        student (ForeignKey): The student the notification is intended for.
        message (TextField): The message text of the notification.
        date_created (DateTimeField): When the notification was created.
        is_read (BooleanField): Whether the notification has been read or not.
    """

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def mark_as_read(self):
        """
        Marks the notification as read.
        """
        self.is_read = True
        self.save()

    def __str__(self):
        return f"Notification for {self.Student.username}: {self.message[:20]}..."

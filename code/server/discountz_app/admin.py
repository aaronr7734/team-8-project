from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Student, Discount, Category, Notification

admin.site.register(Student, UserAdmin)
admin.site.register(Discount)
admin.site.register(Category)
admin.site.register(Notification)

class DiscountAdmin(admin.ModelAdmin):
    """
    Represents the Discount model in the Django admin interface.

    This custom admin class automatically sets the 'added_by' field to the
    currently logged-in user when a new Discount is created, and excludes the
    field from the admin form to prevent manual editing.

    Attributes:
        exclude (tuple): Fields to be excluded from the admin form.
    """

    exclude = ("added_by",)  # Exclude the 'added_by' field from the form

    def save_model(self, request, obj, form, change):
        """
        Overrides the save_model method to automatically set the 'added_by' field.

        Args:
            request (HttpRequest): The HttpRequest object.
            obj (Discount): The Discount object being saved.
            form (ModelForm): The form for the Discount model.
            change (bool): True if the model is being changed, False if it's being added.
        """
        if not obj.pk:  # Only set 'added_by' for new objects
            obj.added_by = request.user
        super().save_model(request, obj, form, change)

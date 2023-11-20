from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Student, Discount, Category, Notification

admin.site.register(Student, UserAdmin)
admin.site.register(Discount)
admin.site.register(Category)
admin.site.register(Notification)

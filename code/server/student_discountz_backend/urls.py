"""
URL Configuration for the Django Project

This module contains the URL patterns for our entire Django project. It acts as the central hub, 
routing incoming HTTP requests to the appropriate views based on the requested URL.

Attributes:
    urlpatterns (list): A list of URL patterns used by `urlpatterns`.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('discountz_app.urls')),  # Add this line
]

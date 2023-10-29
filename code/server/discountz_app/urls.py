"""
URL Configuration for the discountz_app App

This module contains the URL patterns specific to the discountz_app app. These patterns define
how HTTP requests are routed to the views within the app.

Attributes:
    urlpatterns (list): A list of URL patterns used by `urlpattern`.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, DiscountViewSet, CategoryViewSet, NotificationViewSet, CustomLoginView, register_view

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')
router.register(r'discounts', DiscountViewSet, basename='discount')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'notifications', NotificationViewSet, basename='notification')

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='custom-login'),
    path('register/', register_view, name='register'),
    path('', include(router.urls)),
]

"""
Name: Russell, Abhinav, Arda
Student ID: C0927696, C0926240, C0923184
Date: August 14, 2025
Assignment: CSD 4523 Term Project - Toronto & GTA History Quiz
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('quiz/', views.start_quiz, name='quiz'),
    path('history/', views.history, name='history'),
]

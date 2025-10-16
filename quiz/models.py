"""
Name: Russell, Abhinav, Arda
Student ID: C0927696, C0926240, C0923184
Date: August 14, 2025
Assignment: CSD 4523 Term Project - Toronto & GTA History Quiz
"""
from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_option = models.CharField(
        max_length=1,
        choices=[('A','A'),('B','B'),('C','C'),('D','D')]
    )

    def __str__(self):
        return self.text[:60]

class QuizAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attempts')
    created_at = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0)
    total = models.IntegerField(default=5)

    @property
    def percent(self):
        return int((self.score / self.total) * 100) if self.total else 0

class Response(models.Model):
    attempt = models.ForeignKey(QuizAttempt, on_delete=models.CASCADE, related_name='responses')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=1, choices=[('A','A'),('B','B'),('C','C'),('D','D')], blank=True)
    is_correct = models.BooleanField(default=False)

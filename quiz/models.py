from django.db import models

# Create your models here.


class Exam(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Question(models.Model):
    exam = models.ForeignKey('Exam', on_delete=models.CASCADE)
    description = models.TextField(blank=False, unique=True)
    explanation = models.TextField(blank=False)
    is_multiple_choice = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    is_correct = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

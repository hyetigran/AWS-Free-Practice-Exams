from django.db import models

# Create your models here.


class Exam(models.Model):
    name = models.CharField()
    description = models.CharField()


class Question(models.Model):
    description = models.TextField(blank=False, unique=True)
    explanation = models.TextField(blank=False)
    exam = models.ForeignKey('Exam', on_delete=models.CASCADE)


class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    is_multiple_choice = models.BooleanField()
    is_correct = models.BooleanField()

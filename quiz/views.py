from django.shortcuts import render
from .models import Question
from .serializers import QuizSerializer
from rest_framework import generics
# Create your views here.


class QuizListCreate(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuizSerializer

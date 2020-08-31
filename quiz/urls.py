from django.urls import path
from . import views

urlpatterns = [
    path('api/quiz', views.QuizListCreate.as_view()),
]

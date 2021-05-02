from django.shortcuts import render

from .models import Question
from .serializers import QuestionSerializer
from rest_framework import mixins, serializers
from rest_framework import generics


class QuestionList(generics.ListCreateAPIView):
    """list all questions or generate new one
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    """retrieve, update or delete an instance
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

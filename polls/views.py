from django.contrib.auth import get_user_model
from .models import Question
from .serializers import QuestionSerializer, UserSerializer
from rest_framework import mixins, serializers
from rest_framework import generics


class QuestionList(generics.ListCreateAPIView):
    """list all questions or generate new one
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    """retrieve, update or delete an instance
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class UserList(generics.ListCreateAPIView):
    """list all Users or generate new one
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """retrieve, update or delete an instance
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

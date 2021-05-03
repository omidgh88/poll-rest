from django.db import models
from django.db.models import query
from django.contrib.auth import get_user_model
from rest_framework import fields, serializers

from .models import Question, Choice


class QuestionSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(read_only=True, source='owner.username')

    class Meta:
        model = Question
        fields = ('id', 'title', 'owner', 'is_active')


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'title', 'question_id', 'votes')


class UserSerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all())

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'questions')

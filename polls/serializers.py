from django.db import models
from django.db.models import query
from django.contrib.auth import get_user_model
from rest_framework import fields, serializers

from .models import Question, Choice


class QuestionSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(read_only=True, source='owner.username')
    choices = serializers.HyperlinkedRelatedField(many=True, view_name='choice-detail', read_only=True)

    class Meta:
        model = Question
        fields = ('url', 'id', 'title', 'owner', 'is_active', 'choices')


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('url', 'id', 'title', 'question_id', 'votes')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    questions = serializers.HyperlinkedRelatedField(many=True, view_name='question-detail', read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('url', 'id', 'username', 'questions')

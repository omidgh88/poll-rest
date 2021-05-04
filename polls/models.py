from django.contrib.auth import get_user_model
from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=255, null=False)
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(get_user_model(), related_name='questions', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class Choice(models.Model):
    title = models.CharField(max_length=255, null=False)
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    votes = models.PositiveIntegerField(default=0)
    owner = models.ForeignKey(get_user_model(), related_name='question_choices', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.question.title}: {self.title}"

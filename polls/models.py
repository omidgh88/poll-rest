from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=255, null=False)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title


class Choice(models.Model):
    title = models.CharField(max_length=255, null=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.question.title}: {self.title}"

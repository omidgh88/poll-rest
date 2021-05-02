from django.contrib import admin

from polls.models import Question, Choice


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ('title', )
    list_display = ('title', 'is_active')


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    search_fields = ('title', )
    list_display = ('title', 'question', 'votes')

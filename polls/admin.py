from django.contrib import admin

from .models import Choice, Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ('title', )
    list_display = ('title', 'is_active')


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    search_fields = ('title', )
    list_display = ('title', 'question', 'votes')

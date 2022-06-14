from django.contrib import admin

# Register your models here.

from .models import *

class QuestionsAdmin(admin.ModelAdmin):
    list_display = ["id", "question"]

class AnswersAdmin(admin.ModelAdmin):
    list_display = ["question_id", "answer"]

class CallsAdmin(admin.ModelAdmin):
    list_display = ["phone", "status", "comment"]


admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Answers, AnswersAdmin)
admin.site.register(Calls, CallsAdmin)
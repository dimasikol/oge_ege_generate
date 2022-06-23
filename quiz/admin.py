from django.contrib import admin
from django.utils.safestring import mark_safe

from .models.quiz_result_student import QuizResult

@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    list_display = ('student','question_type')
    readonly_fields = ('student',)
    list_display_links =('student','question_type')


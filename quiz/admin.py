from django.contrib import admin
from django.utils.safestring import mark_safe
from .models.quiz_result_student import QuizResult
from .models.quiz_create import QuizCategory, QuizKlass, Quiz, QuizCreate, QuizAnswerTrue, QuizAnswerFalse
import nested_admin


@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'question_type', 'date_create')
    readonly_fields = ('student',)
    list_display_links = ('student', 'question_type')

"""Блок админки для создания ручного создания вопросов"""

@admin.register(QuizCategory)
class QuizCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(QuizKlass)
class QuizKlassAdmin(admin.ModelAdmin):
    pass



class TrueAnswerInline(nested_admin.NestedTabularInline):
    model = QuizAnswerTrue
    extra = 1


class FalseAnswerInline(nested_admin.NestedTabularInline):
    model = QuizAnswerFalse
    extra = 0


class QuizCreateInline(nested_admin.NestedTabularInline):
    model = QuizCreate
    inlines = [TrueAnswerInline, FalseAnswerInline]
    extra = 1

@admin.register(Quiz)
class QuizAdmin(nested_admin.NestedModelAdmin):
    list_display = ('id','quiz_name','slug_quiz','quizklass','category_quiz')
    list_editable = ('quiz_name','slug_quiz','quizklass','category_quiz')
    model = Quiz
    inlines = [QuizCreateInline]
    extra = 1
    prepopulated_fields = {"slug_quiz":('quiz_name',)}
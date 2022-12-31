from django import forms
from ..models import quiz_create
class QuizCategoryForms(forms.ModelForm):
    class Meta:
        model = quiz_create.QuizCategory
        fields = ['name','slug','image']
class QuizKlassForms(forms.ModelForm):
    class Meta:
        model = quiz_create.QuizKlass
        fields = ['number']
class QuizForms(forms.ModelForm):
    class Meta:
        model = quiz_create.Quiz
        fields = ['quiz_name','slug_quiz']
class QuizCreateForms(forms.ModelForm):
    class Meta:
        model = quiz_create.QuizCreate
        fields = ['question']
class QuizAnswerTrueForms(forms.ModelForm):
    class Meta:
        model = quiz_create.QuizAnswerTrue
        fields=['answer_true']
class QuizAnswerFalseForms(forms.ModelForm):
    class Meta:
        model = quiz_create.QuizAnswerFalse
        fields=['answer_false']
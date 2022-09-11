from django.shortcuts import render
from django.views import View


class ShowQuizType(View):
    def get(self,requests):
        return render(requests,'quiz/template_randomaize_quiz_generation/show_generate_type_quiz.html')
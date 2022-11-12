from django.views import View
from django.shortcuts import render, redirect,HttpResponse
from ..logicquiz import check_test

class GenerateQuizEge(View):
    def get(self,request):
        return render(request,'quiz/template_randomaize_quiz_generation/quiz_ege/quiz_choice.html')

    def post(self,request,*args,**kwargs):
        self.quiz = check_test.context_ege(request.POST)
        return render(request,'quiz/template_randomaize_quiz_generation/quiz_ege/show_quiz.html',self.quiz)


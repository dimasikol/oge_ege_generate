from django.shortcuts import render, redirect
from django.views import View
from ..models import quiz_create
from django.contrib.auth.mixins import LoginRequiredMixin

class QuizCategoryView(View):
    def get(self,requests):
        date = quiz_create.QuizCategory.objects.all()
        return render(requests,'quiz/quiz_create/show_quiz_category.html',context={"category_quiz":date})

class ShowCategoryQuizView(View):
    def get(self,requests,name):
        date = quiz_create.Quiz.objects.filter(category_quiz__slug=name)
        return render(requests,'quiz/quiz_create/show_quiz_category_filter.html',{"quizs":date})


class ShowQuizView(LoginRequiredMixin,View):
    login_url = '/user/login/'

    def get(self,requests,name,quiz,**kwargs):
        date = quiz_create.QuizCreate.objects.filter(category_quiz__slug_quiz=quiz)
        return render(requests,'quiz/quiz_create/show_quiz.html',{"quiz":date})

    def post(self,requests,name,quiz,**kwargs):
        if requests.method=='POST':
            date = quiz_create.QuizCreate.objects.filter(category_quiz__slug_quiz=quiz)
            user_answer = [''.join(item.split(',')) if item.find(',')!=-1 else item for item in requests.POST.getlist('answer')] # список ответов пользователя
            date_answer = [''.join([item.answer_true for item in date[i].question_true.all()]) for i in range(len(date))] # список правильных ответов
            result = [sum([i==k for i,k in zip(user_answer,date_answer)]),len(date_answer)] #

            print(result)
            print(date_answer)
            print(user_answer)
        return redirect('/quiz/quiz_category/computer-science/test5/')



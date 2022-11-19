from django.shortcuts import render, redirect
from django.views import View
from ..models import quiz_create
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework import permissions

class QuizCategoryView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,requests):
        date = quiz_create.QuizCategory.objects.all()
        return render(requests,'quiz/quiz_create/show_quiz_category.html',context={"category_quiz":date})

class ShowCategoryQuizView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,requests,name):
        date = quiz_create.Quiz.objects.filter(category_quiz__slug=name)
        return render(requests,'quiz/quiz_create/show_quiz_category_filter.html',{"quizs":date})


class ShowQuizView(LoginRequiredMixin,View):
    login_url = '/user/login/'

    def get(self,requests,name,quiz,**kwargs):
        date = quiz_create.QuizCreate.objects.filter(category_quiz__slug_quiz=quiz)
        return render(requests,'quiz/quiz_create/show_quiz.html',{"quiz":date})

    def post(self,requests,name,quiz,**kwargs):
        date = quiz_create.QuizCategory.objects.all()
        if requests.method=='POST':
            print(requests.post)


        return render(requests, 'quiz/quiz_create/show_quiz_category_filter.html', {"quizs": date})


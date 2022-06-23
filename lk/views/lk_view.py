import requests
from django.shortcuts import render
from django.views import generic
from quiz.models.quiz_result_student import QuizResult
class LkView(generic.View):

    def get(self,request):
        self.date=QuizResult.objects.all()
        context = {'list_object': self.date}
        print(self.date)
        return render(request,'lk/personal_account/lk.html',context)
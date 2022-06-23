from django.shortcuts import render,redirect
from django.views import generic
from django.http import HttpResponseRedirect
from ..logicquiz import check_test
from ..models.quiz_result_student import QuizResult
import random
import time
class QuizView(generic.View):
    def get(self,request,**kwargs):
        return render(request,"quiz/template_randomaize_quiz_generation/quiz/quiz_choice.html")

class ShowQuizView(generic.View):

    def get(self,request,**kwargs):
        global context
        context = check_test.context(request.GET)
        return render(request,"quiz/template_randomaize_quiz_generation/base.html",context=context)

    def post(self,request,**kwargs):
        global context
        if request.method=='POST': #and str(request.user)!="AnonymousUser":
            answer_all={}
            for type_answer in request.POST:
                if type_answer in context:
                    answer_all[type_answer]=[len(context[type_answer]),0]
                    for i in range(len(context[type_answer])):
                        if isinstance(request.POST[type_answer],list):
                            pass
                        elif str(request.POST[type_answer])==str(context[type_answer][i]['answer']):
                            answer_all[type_answer][1]+=1
                        answer_all[type_answer].append(((request.POST[type_answer]),context[type_answer][i]['answer']))
            base_date=QuizResult(answer=request.POST,student=request.user,question_number="answer1",question_type='oge',quiz =context,result=answer_all)
            base_date.save()
            return render(request,"quiz/template_randomaize_quiz_generation/quiz/quiz_result.html")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




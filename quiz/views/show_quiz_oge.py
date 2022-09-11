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
        if request.method == 'POST': #and str(request.user)!="AnonymousUser":
            answer_all = {}
            starts = 0
            results_fin = [0,0]
            for type_answer in request.POST:
                if type_answer in context:
                    answer_all[type_answer]=[len(context[type_answer]),0]
                    for i in range(len(context[type_answer])):
                        answer_all[type_answer].append({type_answer:[(dict(request.POST)[type_answer][i]),context[type_answer][i]['answer']]})
                        results_fin[0] += 1
                    date = [str(item[type_answer][0])==str(item[type_answer][1]) if isinstance(item,dict) else 0 for item in answer_all[type_answer]]
                    results_fin[1]+=sum(date)
            base_date=QuizResult(answer=dict(request.POST),student=request.user,question_number="answer1",question_type='oge',quiz = context,result=answer_all,result_fin=results_fin)
            base_date.save()
            return render(request,"quiz/template_randomaize_quiz_generation/quiz/quiz_result.html")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



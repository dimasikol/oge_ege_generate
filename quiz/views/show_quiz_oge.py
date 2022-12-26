import requests
from django.shortcuts import render,redirect
from django.views import generic
from django.http import HttpResponseRedirect
import json
from instrumenst.pdf.pdf_creater import create_pdf_at_html
from ..logicquiz import check_test
from ..models.quiz_result_student import QuizResult
from apps.settings import CONTEXT
from rest_framework.views import APIView
from rest_framework import permissions

class QuizView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,**kwargs):
        if request.user in CONTEXT['oge'] and 'timer':
            return render(request, "quiz/template_randomaize_quiz_generation/base.html",context=CONTEXT['oge'][request.user])
        return render(request,"quiz/template_randomaize_quiz_generation/quiz_oge/quiz_choice.html")


class ShowQuizView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,**kwargs):
        # дописать функцию таймера!!!
        if request.user in CONTEXT['oge'] and 'timer':
            if 'send-pdf' in request.GET:
                self.req=render(request, "quiz/template_randomaize_quiz_generation/base.html",context=CONTEXT['oge'][request.user]).content.decode('utf-8')
                self.req2=self.req[:-700]
                r=create_pdf_at_html(self.req2,user_name=request.user.email)
                CONTEXT['oge'][request.user]['create_pdf'] = r
                CONTEXT['oge'][request.user]['counter'] = CONTEXT['oge']['counter']
            return render(request, "quiz/template_randomaize_quiz_generation/base.html",context=CONTEXT['oge'][request.user])

        if sum(list(map(lambda x: int(x) if str(x).isdigit() else 0,list(request.GET.values()))))==0:
            return redirect('quiz:quiz_generate_oge')
        CONTEXT['oge'][request.user] = check_test.context(request.GET)
        CONTEXT['oge'][request.user]['counter'] = CONTEXT['oge']['counter']
        return render(request,"quiz/template_randomaize_quiz_generation/base.html",context=CONTEXT['oge'][request.user])

    def post(self,request,**kwargs):
        if request.method == 'POST': #and str(request.user)!="AnonymousUser":
            answer_all = {}
            results_fin = [0,0]
            for type_answer in request.POST:
                if type_answer in CONTEXT['oge'][request.user]:
                    answer_all[type_answer]=[len(CONTEXT['oge'][request.user][type_answer]),0]
                    for i in range(len(CONTEXT['oge'][request.user][type_answer])):
                        answer_all[type_answer].append({type_answer:[(dict(request.POST)[type_answer][i]),CONTEXT['oge'][request.user][type_answer][i]['answer']]})
                        results_fin[0] += 1
                    date = [str(item[type_answer][0])==str(item[type_answer][1]) if isinstance(item,dict) else 0 for item in answer_all[type_answer]]
                    results_fin[1]+=sum(date)
                    answer_all[type_answer][1]=sum(date)
            base_date=QuizResult(answer=dict(request.POST),student=request.user,question_number="answer1",question_type='oge',quiz = CONTEXT['oge'][request.user],result=answer_all,result_fin=results_fin)
            base_date.save()
            del CONTEXT['oge'][request.user]
            return render(request,"quiz/template_randomaize_quiz_generation/quiz_oge/quiz_result.html")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
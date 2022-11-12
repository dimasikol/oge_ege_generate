from django.shortcuts import render,redirect
from django.views import generic
from django.http import HttpResponseRedirect
from ..logicquiz import check_test
from ..models.quiz_result_student import QuizResult
from apps.settings import CONTEXT

class QuizView(generic.View):
    def get(self,request,**kwargs):
        return render(request,"quiz/template_randomaize_quiz_generation/quiz_oge/quiz_choice.html")


class ShowQuizView(generic.View):

    def get(self,request,**kwargs):
        #global CONTEXT
        if sum(list(map(lambda x: int(x) if str(x).isdigit() else 0,list(request.GET.values()))))==0:
            return redirect('quiz_generate_oge')
        CONTEXT[request.user] = check_test.context(request.GET)

        return render(request,"quiz/template_randomaize_quiz_generation/base.html",context=CONTEXT[request.user])

    def post(self,request,**kwargs):
        #global CONTEXT
        if request.method == 'POST': #and str(request.user)!="AnonymousUser":
            answer_all = {}
            starts = 0
            results_fin = [0,0]
            for type_answer in request.POST:
                if type_answer in CONTEXT[request.user]:
                    answer_all[type_answer]=[len(CONTEXT[request.user][type_answer]),0]
                    for i in range(len(CONTEXT[request.user][type_answer])):
                        answer_all[type_answer].append({type_answer:[(dict(request.POST)[type_answer][i]),CONTEXT[request.user][type_answer][i]['answer']]})
                        results_fin[0] += 1
                    date = [str(item[type_answer][0])==str(item[type_answer][1]) if isinstance(item,dict) else 0 for item in answer_all[type_answer]]
                    results_fin[1]+=sum(date)
                    answer_all[type_answer][1]=sum(date)
            base_date=QuizResult(answer=dict(request.POST),student=request.user,question_number="answer1",question_type='oge',quiz = CONTEXT[request.user],result=answer_all,result_fin=results_fin)
            base_date.save()
            return render(request,"quiz/template_randomaize_quiz_generation/quiz_oge/quiz_result.html")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



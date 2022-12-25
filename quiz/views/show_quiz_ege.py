from django.shortcuts import render, redirect,HttpResponse
from ..logicquiz import check_test
from ..models.quiz_create import QuizCreate
from ..models.quiz_result_student import QuizResult
from apps.settings import CONTEXT
from rest_framework import permissions
from rest_framework.views import APIView
class GenerateQuizEge(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        if request.user in CONTEXT['ege']:
            return render(request, 'quiz/template_randomaize_quiz_generation/quiz_ege/show_quiz.html', CONTEXT['ege'][request.user])
        return render(request,'quiz/template_randomaize_quiz_generation/quiz_ege/quiz_choice.html')

    def post(self,request,*args,**kwargs):
        self.quiz = QuizCreate.objects.all()
        if 'choice' in request.POST and request.method == 'POST':
            self.data={}
            for i in range(28):
                if f'quiz{i}' in request.POST:
                    self.shuffle=self.quiz.filter(type_ege=i).order_by('?')[:int(request.POST[f'quiz{i}'])]
                    self.data[f'quiz{i}'] = self.shuffle
            CONTEXT['ege'][request.user]=self.data
            return render(request,'quiz/template_randomaize_quiz_generation/quiz_ege/show_quiz.html', self.data)

        if 'answer' in request.POST and request.method == 'POST':
            answer_all = {}
            results_fin = [0, 0]
            answer_user = dict(request.POST)
            for type_answer in request.POST:
                if type_answer in CONTEXT['ege'][request.user]:
                    answer_all[type_answer]=[len(CONTEXT['ege'][request.user][type_answer]),0]
                    for i in range(len(CONTEXT['ege'][request.user][type_answer])):
                        if str(answer_user[type_answer][i]) == str(CONTEXT['ege'][request.user][type_answer][i].question_true.all()[0]):
                            answer_all[type_answer][1] += 1
                            results_fin[1]+=1
                        results_fin[0]+=1
            base_date = QuizResult(answer=answer_user,student=request.user,question_number='answer2',question_type='ege',quiz=CONTEXT['ege'][request.user],result=answer_all,result_fin=results_fin)
            base_date.save()
            del CONTEXT['ege'][request.user]
            return redirect('lk:home')
        return redirect('lk:home')


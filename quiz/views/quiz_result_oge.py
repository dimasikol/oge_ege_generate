from rest_framework.views import APIView
from ..models.quiz_result_student import QuizResult
from django.shortcuts import render
from ..serializers import QuizResultSerializers
from rest_framework import permissions

class StatisticOgeView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    DATA_OGE=['answer1','answer2','answer3','answer4','answer5','answer6','answer7','answer8','answer9','answer10']
    def get(self,request):
        self.data_oge={}
        self.data_for_table_oge = [[0] * 10, [0] * 10]
        self.quiz_result_oge=QuizResult.objects.filter(question_type='oge')
        for users in set(list(map(lambda x: x['student'],self.quiz_result_oge.values('student')))):
            self.data_oge[users] = {answer:[0,0] for answer in StatisticOgeView.DATA_OGE}

        for quiz in self.quiz_result_oge:
             self.result = eval(quiz.result)
             for self.key in self.result.keys():
                self.data_oge[quiz.student][self.key] = [self.data_oge[quiz.student][self.key][0]+self.result[self.key][0],self.data_oge[quiz.student][self.key][1]+self.result[self.key][1]]
                self.data_for_table_oge[0][int(self.key[-1]) - 1]+=self.result[self.key][0]
                self.data_for_table_oge[1][int(self.key[-1]) - 1]+=self.result[self.key][1]

        return render(request,'quiz/quiz_result/show_all_result_user.html', context={'object_list':self.data_oge,'date_table':self.data_for_table_oge})


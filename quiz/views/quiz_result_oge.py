from django.views import View
from ..models.quiz_result_student import QuizResult
from django.shortcuts import render
from ..serializers import QuizResultSerializers

class StatisticOgeView(View):
    DATA=['answer1','answer2','answer3','answer4','answer5','answer6','answer7','answer8','answer9','answer10']
    def get(self,request):
        self.data={}
        self.data_for_table = [[0]*10, [0]*10]
        self.quiz_result=QuizResult.objects.all()
        for users in set(list(map(lambda x: x['student'],self.quiz_result.values('student')))):
            self.data[users] = {answer:[0,0] for answer in StatisticOgeView.DATA}
        for quiz in self.quiz_result:
             self.result = eval(quiz.result)
             for self.key in self.result.keys():
                self.data[quiz.student][self.key] = [self.data[quiz.student][self.key][0]+self.result[self.key][0],self.data[quiz.student][self.key][1]+self.result[self.key][1]]
                self.data_for_table[0][int(self.key[-1])-1]+=self.result[self.key][0]
                self.data_for_table[1][int(self.key[-1])-1]+=self.result[self.key][1]
        print(self.data_for_table)
        return render(request,'quiz/quiz_result/show_all_result_user.html',context={'object_list':self.data,'date_table':self.data_for_table })

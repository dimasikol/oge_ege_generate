from rest_framework.views import APIView
from ..models.quiz_result_student import QuizResult
from django.shortcuts import render
from rest_framework import permissions


class StatisticEgeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    DATA_EGE = ['answer1', 'answer2', 'answer3', 'answer4', 'answer5', 'answer6', 'answer7', 'answer8', 'answer9',
                'answer10', 'answer11', 'answer12', 'answer13', 'answer14', 'answer15','answer16','answer17','answer18', 'answer19',
                'answer20', 'answer21', 'answer22','answer23','answer24','answer25','answer26','answer27']

    def get(self, request):
        self.data_ege = {}
        self.data_for_table_ege = [[0] * 27, [0] * 27]
        self.quiz_result_ege = QuizResult.objects.filter(question_type='ege')
        for users in set(list(map(lambda x: x['student'], self.quiz_result_ege.values('student')))):
            self.data_ege[users] = {answer: [0, 0] for answer in StatisticEgeView.DATA_EGE}

        for quiz in self.quiz_result_ege:
            self.result = eval(quiz.result)
            for self.key in self.result.keys():
                self.key2=self.key.replace('quiz','answer')
                self.data_ege[quiz.student][self.key2] = [self.data_ege[quiz.student][self.key2][0] + self.result[self.key][0],    self.data_ege[quiz.student][self.key2][1] + self.result[self.key][1]]
                self.num = int(self.key[-1]) if self.key[-2]=='z' else int(self.key[-2:])
                self.data_for_table_ege[0][self.num - 1] += self.result[self.key][0]
                self.data_for_table_ege[1][self.num - 1] += self.result[self.key][1]
        return render(request, 'quiz/quiz_result/show_all_result_ege.html',context={'object_list': self.data_ege,'date_table_ege': self.data_for_table_ege})


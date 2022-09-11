from django.db import models
from picklefield.fields import PickledObjectField


class QuizResult(models.Model):
    answer = PickledObjectField()
    question_number = models.CharField(max_length=20)
    question_type = models.CharField(max_length=20)
    student = models.CharField(max_length=30)
    token = models.CharField(max_length=1000, blank=True, default='0')
    result = models.CharField(max_length=1000)
    quiz = PickledObjectField()
    result_fin = models.CharField(max_length=100, default='')
    date_create = models.DateTimeField(auto_now=True)

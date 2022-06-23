from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class QuizCategory(models.Model):
    category_quiz = models.CharField(max_length=40)

class QuizCreate(models.Model):
    category_quiz = models.ForeignKey(QuizCategory,on_delete=models.CASCADE)
    name = models.CharField(max_length=40, unique=True)
    question = RichTextUploadingField()

class Answer(models.Model):
    answer = models.CharField(max_length=1000)
    question = models.ForeignKey(QuizCreate,on_delete=models.CASCADE)

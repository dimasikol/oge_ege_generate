from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import random

class QuizCategory(models.Model):
    name = models.CharField(verbose_name='имя категории',max_length=40,unique=True)
    slug = models.SlugField(max_length=80)
    image = models.ImageField(verbose_name='фото категории',upload_to='media/quiz/quiz_category/',blank=True,default='')


    def __str__(self):
        return f'{self.name}'


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class QuizKlass(models.Model):
    number = models.PositiveIntegerField(verbose_name='номер класса')
    def __str__(self):
        return f'{self.number}'
    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'


class Quiz(models.Model):
    quiz_name = models.CharField(verbose_name='название теста',max_length=40)
    slug_quiz = models.SlugField(verbose_name='ссылка на тест',max_length=80,unique=True)
    quizklass = models.ForeignKey(QuizKlass,on_delete=models.DO_NOTHING,blank=True,verbose_name='Класс')
    category_quiz = models.ForeignKey(QuizCategory,on_delete=models.DO_NOTHING,blank=True,verbose_name='Категория')

    def __str__(self):
        return f'{self.category_quiz} {self.quiz_name}'

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class QuizCreate(models.Model):
    category_quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name='quizes')
    question = RichTextUploadingField(verbose_name='вопрос')
    type_ege = models.IntegerField(default=0,blank=True)

    def __str__(self):
        return f'{self.pk}'
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'вопросы'

class QuizAnswerTrue(models.Model):
    answer_true = models.CharField(verbose_name='правильный ответ',max_length=1000)
    quiz_true = models.ForeignKey(QuizCreate,on_delete=models.CASCADE,related_name='question_true')
    class Meta:
        verbose_name = 'Правильный ответ'
        verbose_name_plural = 'Правильные ответы'
    def __str__(self):
        return self.answer_true

class QuizAnswerFalse(models.Model):
    answer_false = models.CharField(verbose_name='ложный ответ',max_length=1000)
    quiz_false = models.ForeignKey(QuizCreate,on_delete=models.CASCADE,related_name='question_false')
    class Meta:
        verbose_name = 'Ложный ответ'
        verbose_name_plural = 'Ложные ответы'

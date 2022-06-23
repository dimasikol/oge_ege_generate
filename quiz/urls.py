from django.urls import path
from .views import show_quiz


urlpatterns = [
    path('', show_quiz.QuizView.as_view()),
    path('<str:get>',show_quiz.ShowQuizView.as_view(),name='quiz_create'),

]




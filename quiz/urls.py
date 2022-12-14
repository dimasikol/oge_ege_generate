from django.urls import path
from .views import show_quiz_oge,show_quiz_create,show_quiz_type, quiz_create,show_quiz_ege,quiz_result_oge,quiz_result_ege


urlpatterns = [
    path('',show_quiz_type.ShowQuizType.as_view(),name='quiz_generate_type'),
    path('oge/', show_quiz_oge.QuizView.as_view(),name='quiz_generate_oge'),
    path('oge/quiz_result_oge/', quiz_result_oge.StatisticOgeView.as_view(), name='quiz_result_oge'),
    path('oge/quiz_result_ege/', quiz_result_ege.StatisticEgeView.as_view(), name='quiz_result_ege'),
    path('oge/<str:get>/', show_quiz_oge.ShowQuizView.as_view(), name='quiz_create'),
    path('ege/',show_quiz_ege.GenerateQuizEge.as_view(),name='quiz_generate_ege'),
    #path('ege/<str:get>/',show_quiz_ege.GenerateQuizEge.as_view(),name='quiz_generate_ege'),

    path('quiz_category/',show_quiz_create.QuizCategoryView.as_view(),name='quiz_category'),
    path('quiz_category/<str:name>/',show_quiz_create.ShowCategoryQuizView.as_view(),name='quiz_category_filter'),
    path('quiz_category/<str:name>/<slug:quiz>/',show_quiz_create.ShowQuizView.as_view(),name='show_quiz'),
    path('quiz_category/<str:name>/<slug:quiz>/',show_quiz_create.ShowQuizView.as_view(),name='send_answer_quiz_create'),

    path('quiz_category_app/', quiz_create.QuizCategoryView.as_view(),name='quiz_create_app'),
    path('quiz_category_app/<slug:quiz>/',quiz_create.QuizCategoryView.as_view(),name='quiz_update_app'),


]




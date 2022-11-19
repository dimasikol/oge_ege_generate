from django.shortcuts import render
from rest_framework import mixins,generics,views
from rest_framework.response import Response
from ..forms import forms_quiz_create
from ..models import quiz_create
from .. import serializers

class QuizCategoryView(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,views.APIView):
    queryset = quiz_create.QuizCategory
    serializer_class = serializers.QuizCategorySerializers

    def get(self,request, *args, **kwargs):
        self.date = QuizCategoryView.queryset.objects.all()
        self.form_create = forms_quiz_create.QuizCategoryForms()
        self.form_update = ''
        return render(request,'quiz/quiz_create/show_quiz_category.html',{'category_quiz':self.date, 'form_create':forms_quiz_create})

    def create(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, kwargs)






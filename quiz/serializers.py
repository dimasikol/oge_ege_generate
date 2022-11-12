from rest_framework import serializers
from .models import quiz_create,quiz_result_student

class QuizCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = quiz_create.QuizCategory
        fields = '__all__'


class QuizResultSerializers(serializers.ModelSerializer):
    class Meta:
        model = quiz_result_student.QuizResult
        fields = ['student','result']
from rest_framework import serializers
from .models import quiz_create

class QuizCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = quiz_create.QuizCategory
        fields = '__all__'
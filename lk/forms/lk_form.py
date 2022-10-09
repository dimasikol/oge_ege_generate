from django import forms
from users.models import Profiles,Clas,Education,AlbomsImage,Friendship


class EditLkForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = ('image_profile','location','about','city','birthday','zodiac','socionics_type','show_profile')

class AlbomsImageForm(forms.ModelForm):
    class Meta:
        model = AlbomsImage
        fields = '__all__'

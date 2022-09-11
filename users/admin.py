from django.contrib import admin
from .models import Profiles,Education,Clas,AlbomsImage,Friendship

@admin.register(Profiles)
class AdminProfiles(admin.ModelAdmin):
    pass

admin.register(Education,Clas,AlbomsImage,Friendship)(admin.ModelAdmin)



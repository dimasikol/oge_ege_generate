from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import NewsCategoryModel,PostNewsCategoryModel

@admin.register(NewsCategoryModel)
class AdminNewsCategory(admin.ModelAdmin):
    list_display = ('pk','name','slug','get_image')
    list_editable = ('name','slug')
    def get_image(self,obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50" height="60"/>')
    get_image.allow_rags=True

@admin.register(PostNewsCategoryModel)
class AdminPostNewsCategory(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug','get_image')
    list_editable = ('name', 'slug')
    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50" height="60"/>')

    get_image.allow_rags = True

# Register your models here.

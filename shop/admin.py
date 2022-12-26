from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import model,category,subcategory,item

@admin.register(item.Items)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('pk','name','get_image','model','price','skidka','count','url')
    list_editable = ('name','model','count','price','skidka','url')
    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50" height="60"/>')
    get_image.allow_tags = True
    save_on_top = True

@admin.register(item.ImageItems)
class ImageItemAdmin(admin.ModelAdmin):
    pass


@admin.register(item.ReviewsItem)
class ReviewsItemAdmin(admin.ModelAdmin):
    pass


@admin.register(model.Model)
class ModelItemAdmin(admin.ModelAdmin):
    pass


@admin.register(category.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(subcategory.SubCategory)
class SubcategoryAdmin(admin.ModelAdmin):
    pass


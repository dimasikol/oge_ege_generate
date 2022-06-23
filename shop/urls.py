from django.urls import path
from .views import category,subcategory,item
urlpatterns = [
    path('',category.CategoryView.as_view(),name = 'category'),
    path('<slug:url>/',subcategory.SubCategoryView.as_view(),name='subcategory'),
    path('<slug:url>/<slug:item_url>/',item.ItemsView.as_view(),name='items'),
    path('<slug:url>/<slug:item_url>/<slug:items_url>/',item.ItemsDetailView.as_view(),name='item'),


]
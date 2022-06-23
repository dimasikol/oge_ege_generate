from django.shortcuts import render
from django.views import generic
from ..models.category import Category
class CategoryView(generic.ListView):
    model = Category
    template_name = "shop/temp/list_category.html"


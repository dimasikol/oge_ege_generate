from django.views import generic
from django.shortcuts import render
from ..models.subcategory import SubCategory
class SubCategoryView(generic.ListView):
    model = SubCategory
    def get(self,request,**kwargs):
        self.date = SubCategory.objects.filter(category__url = kwargs['url'])
        return render(request,template_name='shop/temp/list_sub_category.html',context={"object_list":self.date })
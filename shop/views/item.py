from  django.views import generic
from ..models import item
from django.shortcuts import render
class ItemsView(generic.ListView):
    model = item.Items
    def get(self,requests,**kwargs):
        self.date = item.Items.objects.filter(sub_category_id__slug=kwargs['item_url'])
        return render(requests,template_name="shop/temp/list_item_category.html",context={"object_list":self.date})

class ItemsDetailView(generic.DetailView):
    model = item.Items
    template_name = 'shop/temp/items_detail.html'
    def get(self,requests,**kwargs):
        self.date = item.Items.objects.get(url=kwargs['items_url'])
        return render(requests,template_name='shop/temp/items_detail.html',context={'object':self.date})

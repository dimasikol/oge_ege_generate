from django.urls import path
from .views.lk_view import LkView

urlpatterns = [
    path('',LkView.as_view(),name='personal_account')

]

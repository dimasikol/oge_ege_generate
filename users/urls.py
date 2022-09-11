import django.contrib.auth
from django.urls import path
from . import views
urlpatterns = [
    path('sign-up/', views.sign_up,name='sing_up'),

    path('authenticate/',django.contrib.auth.authenticate,name='authenticate'),

    path('login/',views.login_view,name='login'),
    path('logout/',views.logoutview,name='logout'),

    path('users/',views.ShowAllPeople.as_view(),name='show_all_people')
]

#    path('rename/',views.rename_user,name='rename'),

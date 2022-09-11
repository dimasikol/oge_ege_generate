from django.shortcuts import render, redirect
from djoser.conf import User
from rest_framework import permissions
from rest_framework.views import APIView
from .forms import RegisterForm,AccountAuthenticationForm # RenameForm, RenameFormProfile
from django.contrib.auth import login, logout, authenticate
from .models import Profiles

def sign_up(requests):
    """Регистрация"""
    if requests.method == 'POST':
        form = RegisterForm(requests.POST)
        if form.is_valid():
            user = form.save()
            login(requests, user)
            profiles=Profiles(user=user)
            profiles.save()
            return redirect('/accounts/profile/')
    else:
        form = RegisterForm()
    return render(requests, 'registration/sign-up.html', {"form": form})


def login_view(requests,*args,**kwargs):
    context={}
    user = requests.user
    if user.is_authenticated:
        return redirect('home')
    if requests.POST:
        form = AccountAuthenticationForm(requests.POST)
        if form.is_valid():
            username = requests.POST['username']
            password = requests.POST['password']
            user = authenticate(username=username,password=password)
            if user:
                login(requests,user)
                destination = get_redirect_if_exists(requests)
                if destination:
                    return redirect(destination)
                return redirect('home')
        else:
            context['login_form'] = form
    return render(requests,template_name='registration/login.html',context=context)

def get_redirect_if_exists(requests):
    redirect = None
    if requests.GET:
        if requests.GET.get('next'):
            redirect = str(requests.GET.get('next'))
    return redirect


def logoutview(requests):
    if requests.user.is_authenticated:
        print(requests.user)
        logout(requests)
    return redirect('home')


class ShowAllPeople(APIView):
    """вьюха в личных кабинетак пользователей/ для показа всех пользователей"""
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        users = User.objects.all()
        return render(request, 'user_templates/show_all_users.html',
                      {'users': users})

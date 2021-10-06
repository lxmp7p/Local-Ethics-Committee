from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import ListView, DetailView, View
from .functions.userFunc import authorize, addNewUser
from django.contrib.auth import logout


class Registration(View):
    """Регистрация нового пользователя в системе"""
    def get(self, request):
        user_form = UserRegistrationForm()
        return render(request, 'auth/register.html', {'user_form': user_form})

    def post(self, request):
        error = addNewUser(request)
        if error:
           return render(request, 'auth/register.html', {'error': error})
        else:
            return redirect('login')


class Authorization(View):
    """Авторизация в системе"""
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("research/")
        return render(request, 'auth/login.html')

    def post(self, request):
        error = authorize(request)
        if error:
           return render(request, 'auth/login.html', {'error': error})
        else:
            return redirect(reverse('index'))
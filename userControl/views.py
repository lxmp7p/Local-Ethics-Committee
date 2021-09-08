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
        return render(request, 'userControl/register.html', {'user_form': user_form})

    def post(self, request):
        addNewUser(request)
        return redirect('login')


class Authorization(View):
    """Авторизация в системе"""
    def get(self, request):
        form = LoginForm()
        return render(request, 'userControl/login.html', {'form': form})

    def post(self, request):
        error = authorize(request)
        if error:
           return HttpResponse(error) 
        else:
            return redirect(reverse('researchTypeList'))


class Logout(View):
    """Выход из системы"""
    def get(self, request):
        logout(request)
        return redirect('login')


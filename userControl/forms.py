from django import forms
from django.forms import widgets
from .models import User
from django.utils.translation import ugettext_lazy as _


class LoginForm(forms.Form):
    username = forms.CharField(label='Email', widget=forms.EmailInput)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторить пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name','middle_name')

        labels = {
        'username': _('Email'),
        }

      

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
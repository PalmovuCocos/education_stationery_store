from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *


class AddBasketFrom(forms.ModelForm):    # наследование от класса формы модели
    class Meta:    # класс, который связвыет форму с моделью и показывает, какие должны быть поля от модели
        model = Basket
        fields = ['amount']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин')
    password1 = forms.CharField(label='Пароль')
    password2 = forms.CharField(label='Повтор пароля')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')


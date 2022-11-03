from django import forms
from .models import *


class AddBasketFrom(forms.ModelForm):    # наследование от класса формы модели
    class Meta:    # класс, который связвыет форму с моделью и показывает, какие должны быть поля от модели
        model = Basket
        fields = ['amount']

from django import forms
from .models import *


class AddBasketFrom(forms.ModelForm):
    class Meta:
        model = Basket
        fields = ['amount']

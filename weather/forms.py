from django import forms
from django.forms import CharField, TextInput


class Add_cityForm(forms.Form):
    """Форма быстрого поиска."""

    country = CharField(label='Введите страну', widget=TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Поиск', 'cols': 70, 'rows': 10}
        ))
    city = CharField(label='Введите город', widget=TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Поиск', 'cols': 70, 'rows': 10}
        ))

from django.forms import ModelForm
from django import forms
from .models import MyUser


class UserCreateForm(ModelForm):

    class Meta:
        model = MyUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'birthday_date']
        widgets = {
                    'birthday_date': forms.DateInput(attrs={'class': 'datepicker'})
                }

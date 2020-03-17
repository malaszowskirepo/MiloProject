from django.forms import ModelForm
from django import forms
from .models import MyUser
from django.contrib.admin.widgets import AdminDateWidget



class UserCreateForm(ModelForm):

    class Meta:
        model = MyUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'birthday_date']
        widgets = {
                    'birthday_date': forms.DateInput(attrs={'class': 'datepicker', 'id': 'data_input'})
                }

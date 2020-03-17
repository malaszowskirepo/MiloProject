from django.shortcuts import render
from .forms import UserCreateForm
from django.views.generic.edit import CreateView
from MiloApplication import models


class AddUser(CreateView):
    model = models.MyUser
    template_name = 'MiloApplication/add-user.html'
    form_class = UserCreateForm

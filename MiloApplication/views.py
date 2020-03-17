from django.urls import reverse_lazy
from .forms import UserCreateForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from MiloApplication.models import MyUser


class AddUser(CreateView):
    model = MyUser
    template_name = 'MiloApplication/add-user.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('milo_app:all-users')


class AllUsers(ListView):
    model = MyUser
    template_name = 'MiloApplication/user-list.html'
    context_object_name = 'user_list'


class EditUser(UpdateView):
    model = MyUser
    template_name = 'MiloApplication/edit-user.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('milo_app:all-users')


class DeleteUser(DeleteView):
    model = MyUser
    template_name = 'MiloApplication/delete-user.html'
    success_url = reverse_lazy('milo_app:all-users')


class UserDetails(DetailView):
    model = MyUser
    template_name = 'MiloApplication/user-details.html'
    context_object_name = 'user'

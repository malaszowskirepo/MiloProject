from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import UserCreateForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from MiloApplication.models import MyUser
import csv
from .templatetags import user_tags


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


def render_to_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'
    writer = csv.writer(response, delimiter=';')
    writer.writerow(['Username' , 'Birthday ', 'Eligible ', 'Random Number', 'BizzFuzz'])
    all_users = MyUser.objects.all()
    for user in all_users:
        eligible = user_tags.is_under_13(user.birthday_date)
        blizzfuzz = user_tags.bizz_fuzz(user.random_number_field)
        writer.writerow([user.username, user.birthday_date, eligible, user.random_number_field, blizzfuzz])
    return response

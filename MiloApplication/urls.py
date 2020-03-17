from django.urls import path
from . import views

app_name = 'milo_app'

urlpatterns = [
    path('add-user/', views.AddUser.as_view(), name='add-user'),

]
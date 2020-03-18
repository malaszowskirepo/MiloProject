from django.urls import path
from . import views

app_name = 'milo_app'

urlpatterns = [
    path('add-user/', views.AddUser.as_view(), name='add-user'),
    path('all-users/', views.AllUsers.as_view(), name='all-users'),
    path('edit-user/<int:pk>', views.EditUser.as_view(), name='edit-user'),
    path('delete-user/<int:pk>', views.DeleteUser.as_view(), name='delete-user'),
    path('user-details/<int:pk>', views.UserDetails.as_view(), name='user-details'),
    path('render-to-csv', views.render_to_csv, name='render-to-csv'),
]

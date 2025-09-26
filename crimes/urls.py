from django.urls import path
from . import views

urlpatterns = [
    path('input/ipc/', views.ipc_input_view, name='ipc_input'),
    path('input/crime/', views.crime_input_view, name='crime_input'),
    path('login/', views.log_in, name='login'),
    path('register/', views.register, name='register'),
    path('logout/user<str:idd>', views.logout, name='logout'),
    path('', views.view, name='crime'),
]

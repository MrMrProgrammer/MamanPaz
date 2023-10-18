from django.urls import path
from . import views

urlpatterns = [
    path('EmployeeRegister', views.EmployeeRegisterView.as_view(), name='EmployeeRegister'),
    # path('UpdateUserProfile', views.UserUpdateProfileView.as_view(), name='UpdateUserProfile'),
]

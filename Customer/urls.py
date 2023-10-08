from django.urls import path
from . import views

urlpatterns = [
    path('CustomerRegister', views.CustomerRegisterView.as_view(), name='CustomerRegisterView'),
    path('UpdateUserProfile', views.UserUpdateProfileView.as_view(), name='UpdateUserProfile'),
]

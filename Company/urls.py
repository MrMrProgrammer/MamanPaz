from django.urls import path
from . import views

urlpatterns = [
    path('CompanyRegister', views.CompanyRegisterView.as_view(), name='CompanyRegister')
]

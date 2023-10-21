from django.urls import path
from . import views

urlpatterns = [
    path('CompanyRegister', views.CompanyRegisterView.as_view(), name='CompanyRegister'),
    path('UpdateCompanyProfile', views.CompanyUpdateProfileView.as_view(), name='UpdateCompanyProfile'),
    path('AddToSchedule', views.add_to_schedule, name='AddToSchedule'),
    path('ShowSchedule', views.show_schedule, name='ShowSchedule'),
    path('RemoveFromSchedule/<item_id>', views.remove_from_schedule, name='RemoveFromSchedule'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('EmployeeRegister', views.EmployeeRegisterView.as_view(), name='EmployeeRegister'),
    path('UpdateEmployeeProfile/<int:user_id>', views.UpdateEmployeeProfileView.as_view(), name='UpdateEmployeeProfile'),
    path('EmployeeList', views.per_company_employees_list, name='EmployeeList'),
    path('RemoveEmployee/<int:user_id>', views.remove_employee, name='RemoveEmployee'),
]

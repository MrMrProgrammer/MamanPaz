from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View
from .forms import EmployeeRegisterForm
from BaseApp.models import User
from Employee.models import EmployeeModel
from Company.models import CompanyModel


# Create your views here.

class EmployeeRegisterView(View):

    def get(self, request):
        register_form = EmployeeRegisterForm()

        context = {
            'register_form': register_form
        }

        return render(request, 'Employee/EmployeeRegiater.html', context)

    def post(self, request: HttpRequest):

        company: CompanyModel = CompanyModel.objects.filter(user_id=request.user.id).first()

        success_message = 'رمز عبور موقت به آدرس ایمیل شما فرستاده شد.'

        register_form = EmployeeRegisterForm(request.POST)

        if register_form.is_valid():
            employee_email = register_form.cleaned_data.get('email')
            employee: bool = User.objects.filter(email__iexact=employee_email).exists()

            if employee:
                register_form.add_error('email', 'ایمیل وارد شده تکراری می باشد')

            else:
                # email_active_code = str(random.randint(10000000, 99999999))
                email_active_code = '13101380'
                first_name = register_form.cleaned_data.get('first_name')
                last_name = register_form.cleaned_data.get('last_name')
                phone_number = register_form.cleaned_data.get('phone_number')

                new_user = User(is_mom=False,
                                email=employee_email,
                                first_name=first_name,
                                last_name=last_name,
                                phone_number=phone_number,
                                username=employee_email,
                                email_active_code=email_active_code
                                )

                new_user.set_password(email_active_code)

                # send_email("رمز عبور موقت", mom_email, {'email_active_code': email_active_code},"SendMail/RegisterMail.html")

                new_user.save()

                new_user_id = new_user.id

                new_employee = EmployeeModel(company_id=company.id,
                                             user_id=new_user_id)

                new_employee.save()

                context = {
                    'success_message': success_message,
                    'user_name': first_name
                }

                return redirect('home')

                # return render(request, 'Employee/EmployeeRegiater.html', context)

        context = {
            'register_form': register_form,
        }

        return render(request, 'Employee/EmployeeRegiater.html', context)


def PerCompanyEmployeesList(request):

    employees: EmployeeModel = EmployeeModel.objects.filter(company_id = request.user.id).order_by('-id')

    context = {
        "employees": employees,
    }

    return render(request, 'Employee/EmployeesList.html', context)

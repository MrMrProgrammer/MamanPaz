from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import CompanyRegisterForm
from BaseApp.models import User
from SendMail.sendMail import send_email
from .models import CompanyModel, CompanySchedule
from .forms import UpdateCompanyProfileForm, UpdateAdditionalCompanyProfileForm


# Create your views here.


class CompanyRegisterView(View):

    def get(self, request):
        register_form = CompanyRegisterForm()
        context = {
            'register_form': register_form
        }

        return render(request, 'Company/CompanyRegiater.html', context)

    def post(self, request):

        success_message = 'رمز عبور موقت به آدرس ایمیل شما فرستاده شد.'

        register_form = CompanyRegisterForm(request.POST)

        if register_form.is_valid():
            company_email = register_form.cleaned_data.get('email')
            company: bool = User.objects.filter(email__iexact=company_email).exists()

            if company:
                register_form.add_error('email', 'ایمیل وارد شده تکراری می باشد')

            else:
                # email_active_code = str(random.randint(10000000, 99999999))
                company_name = register_form.cleaned_data.get('company_name')
                first_name = register_form.cleaned_data.get('first_name')
                last_name = register_form.cleaned_data.get('last_name')
                email_active_code = '13101380'
                phone_number = register_form.cleaned_data.get('phone_number')
                number = register_form.cleaned_data.get('number')
                numberـpersonnel = register_form.cleaned_data.get('numberـpersonnel')
                address = register_form.cleaned_data.get('address')

                new_company = User(is_company=True,
                                   email=company_email,
                                   first_name=first_name,
                                   last_name=last_name,
                                   phone_number=phone_number,
                                   username=company_email,
                                   email_active_code=email_active_code,
                                   address=address)

                new_company.set_password(email_active_code)

                # send_email("رمز عبور موقت", company_email, {'email_active_code': email_active_code},"SendMail/RegisterMail.html")

                new_company.save()

                company_id = new_company.id

                new_company_model: CompanyModel = CompanyModel(
                    user_id=company_id,
                    company_name=company_name,
                    company_number=number,
                    employee_count=numberـpersonnel,
                )

                new_company_model.save()

                context = {
                    'success_message': success_message
                }

                return render(request, 'Moms/RegisterEmailSent.html', context)

        context = {
            'register_form': register_form,
        }

        return render(request, 'Company/CompanyRegiater.html', context)


class CompanyUpdateProfileView(View):

    def get(self, request: HttpRequest):

        if request.user.is_company:

            current_user = User.objects.filter(id=request.user.id).first()
            current_user_pro = CompanyModel.objects.filter(user_id=request.user.id).first()

            edit_form = UpdateCompanyProfileForm(instance=current_user)
            edit_form_pro = UpdateAdditionalCompanyProfileForm(instance=current_user_pro)

            context = {
                'edit_form': edit_form,
                'edit_form_pro': edit_form_pro,
            }

            return render(request, 'Company/CompanyUpdateProfile.html', context)

        else:
            return HttpResponse('You are not allowed to access this page !')

    def post(self, request: HttpRequest):

        current_user = User.objects.filter(id=request.user.id).first()
        current_pro_user = CompanyModel.objects.filter(user_id=request.user.id).first()

        edit_form = UpdateCompanyProfileForm(request.POST, instance=current_user)
        edit_pro_form = UpdateAdditionalCompanyProfileForm(request.POST, instance=current_pro_user)

        if edit_form.is_valid() and edit_pro_form.is_valid():
            edit_form.save(commit=True)
            edit_pro_form.save(commit=True)

            return redirect('home')

        context = {
            'edit_form': edit_form,
            'edit_pro_form': edit_pro_form,
        }

        return render(request, 'Company/CompanyUpdateProfile.html', context)


def add_to_schedule(request: HttpRequest):
    date = request.GET.get('date')
    user_id = request.GET.get('user_id')
    food_id = request.GET.get('food_id')

    company = CompanyModel.objects.filter(user_id=user_id).first()

    print(date)
    print(user_id)
    print(food_id)

    new_schedule: CompanySchedule = CompanySchedule(
        company_id=company.id,
        food_id=food_id,
        date=date,
    )

    new_schedule.save()

    return HttpResponse('added !')

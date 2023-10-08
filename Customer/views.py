from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomerRegisterForm, UpdateUserProfileForm
from BaseApp.models import User
import random
from SendMail.sendMail import send_email
from django.http import HttpRequest, HttpResponse


# Create your views here.

class CustomerRegisterView(View):

    def get(self, request):
        register_form = CustomerRegisterForm()

        context = {
            'register_form': register_form
        }

        return render(request, 'Customer/CustomersRegiater.html', context)

    def post(self, request):

        success_message = 'رمز عبور موقت به آدرس ایمیل شما فرستاده شد.'

        register_form = CustomerRegisterForm(request.POST)

        if register_form.is_valid():
            mom_email = register_form.cleaned_data.get('email')
            mom: bool = User.objects.filter(email__iexact=mom_email).exists()

            if mom:
                register_form.add_error('email', 'ایمیل وارد شده تکراری می باشد')

            else:
                email_active_code = str(random.randint(10000000, 99999999))
                first_name = register_form.cleaned_data.get('first_name')
                last_name = register_form.cleaned_data.get('last_name')
                phone_number = register_form.cleaned_data.get('phone_number')
                address = register_form.cleaned_data.get('address')

                new_mom = User(is_mom=False,
                               email=mom_email,
                               first_name=first_name,
                               last_name=last_name,
                               phone_number=phone_number,
                               username=mom_email,
                               email_active_code=email_active_code,
                               address=address)

                new_mom.set_password(email_active_code)

                send_email("رمز عبور موقت", mom_email, {'email_active_code': email_active_code},
                           "SendMail/RegisterMail.html")
                new_mom.save()

                context = {
                    'success_message': success_message,
                    'user_name': first_name
                }

                return render(request, 'Customer/RegisterEmailSent.html', context)

        context = {
            'register_form': register_form,
        }

        print('5')

        return render(request, 'Moms/MomsRegiater.html', context)


class UserUpdateProfileView(View):

    def get(self, request: HttpRequest):

        if not request.user.is_mom:
            current_user = User.objects.filter(id=request.user.id).first()

            edit_form = UpdateUserProfileForm(instance=current_user)

            context = {
                'edit_form': edit_form,
            }

            return render(request, 'Customer/CustomersUpdateProfile.html', context)

        else:
            return HttpResponse('You are not allowed to access this page !')

    def post(self, request: HttpRequest):

        current_user = User.objects.filter(id=request.user.id).first()

        edit_form = UpdateUserProfileForm(request.POST, instance=current_user)

        if edit_form.is_valid():
            edit_form.save(commit=True)

            return redirect('home')

        context = {
            'edit_form': edit_form,
        }

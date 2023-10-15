from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from BaseApp.models import User
from .forms import MomRegisterForm, UpdateMomProfileForm, UpdateAdditionalMomProfileForm
from SendMail.sendMail import send_email
from django.http import HttpRequest, HttpResponse
from .models import MomsModel
from Food.models import FoodsModel


# import random


class MomsRegisterView(View):

    def get(self, request):
        register_form = MomRegisterForm()
        context = {
            'register_form': register_form
        }

        return render(request, 'Moms/MomsRegiater.html', context)

    def post(self, request):

        success_message = 'رمز عبور موقت به آدرس ایمیل شما فرستاده شد.'

        register_form = MomRegisterForm(request.POST)

        if register_form.is_valid():
            mom_email = register_form.cleaned_data.get('email')
            mom: bool = User.objects.filter(email__iexact=mom_email).exists()

            if mom:
                register_form.add_error('email', 'ایمیل وارد شده تکراری می باشد')

            else:
                # email_active_code = str(random.randint(10000000, 99999999))
                email_active_code = '13101380'
                first_name = register_form.cleaned_data.get('first_name')
                last_name = register_form.cleaned_data.get('last_name')
                phone_number = register_form.cleaned_data.get('phone_number')
                address = register_form.cleaned_data.get('address')

                new_mom = User(is_mom=True,
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

                mom_id = new_mom.id

                new_mom_model = MomsModel(
                    user_id=mom_id
                )

                new_mom_model.save()

                context = {
                    'success_message': success_message
                }

                return render(request, 'Moms/RegisterEmailSent.html', context)

        context = {
            'register_form': register_form,
        }

        return render(request, 'Moms/MomsRegiater.html', context)


class MomUpdateProfileView(View):

    def get(self, request: HttpRequest):

        if request.user.is_mom:

            current_user = User.objects.filter(id=request.user.id).first()
            current_user_pro = MomsModel.objects.filter(user_id=request.user.id).first()

            edit_form = UpdateMomProfileForm(instance=current_user)
            edit_form_pro = UpdateAdditionalMomProfileForm(instance=current_user_pro)

            context = {
                'edit_form': edit_form,
                'edit_form_pro': edit_form_pro,
                'current_user_pro': current_user_pro,
            }

            return render(request, 'Moms/MomsUpdateProfile.html', context)

        else:
            return HttpResponse('You are not allowed to access this page !')

    def post(self, request: HttpRequest):

        current_user = User.objects.filter(id=request.user.id).first()
        current_pro_user = MomsModel.objects.filter(user_id=request.user.id).first()

        edit_form = UpdateMomProfileForm(request.POST, instance=current_user)
        edit_pro_form = UpdateAdditionalMomProfileForm(request.POST, request.FILES, instance=current_pro_user)

        if edit_form.is_valid() and edit_pro_form.is_valid():
            edit_form.save(commit=True)
            edit_pro_form.save(commit=True)

            return redirect('home')

        context = {
            'edit_form': edit_form,
            'edit_pro_form': edit_pro_form,
        }

        return render(request, 'Moms/MomsUpdateProfile.html', context)


class MomsListView(ListView):
    model = MomsModel
    template_name = 'Moms/MomsListView.html'
    queryset = MomsModel.objects.all()
    context_object_name = 'moms'
    paginate_by = 4


def mom_profile(request, mom_id):
    mom = MomsModel.objects.get(user_id=mom_id)
    foods = FoodsModel.objects.filter(mom__user_id=mom_id)

    context = {
        'mom': mom,
        'foods': foods,
    }

    return render(request, 'Moms/MomsProfile.html', context)


def get_mom_profile(request, mom_id):
    mom = MomsModel.objects.filter(id=mom_id).first()
    profile = mom.profile_photo.url
    return redirect(profile)


def show_mom_wallet(request):
    mom: MomsModel = MomsModel.objects.filter(user_id=request.user.id).first()
    wallet = mom.wallet

    mom_name = mom.user.first_name

    context = {
        'wallet': wallet,
        'mom_name': mom_name
    }

    return render(request, 'Moms/MomWallet.html', context)

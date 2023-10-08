from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views import View
from .forms import LoginForm
from .models import User
from django.http import HttpRequest


def home(request):
    context = {
        'request': request
    }
    return render(request, 'BaseApp/index.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')


class LoginView(View):

    def get(self, request):

        login_form = LoginForm()

        context = {
            'login_form': login_form
        }

        return render(request, 'BaseApp/Login.html', context)

    def post(self, request: HttpRequest):

        login_form = LoginForm(request.POST)

        if login_form.is_valid():

            email = login_form.cleaned_data.get('email')
            password = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=email).first()
            # user_name: User = User.objects.filter(username__iexact=username).first()

            if user is not None:  # or user_name is not None
                is_password_correct = user.check_password(password)

                if is_password_correct:
                    login(request, user)

                    return redirect('home')

                else:
                    login_form.add_error('password', 'ایمیل یا رمز عبور اشتباه است (رمز عبور)')

            else:
                login_form.add_error('password', 'ایمیل یا رمز عبور اشتباه است (ایمیل)')

        context = {
            'login_form': login_form
        }

        return render(request, 'BaseApp/Login.html', context)

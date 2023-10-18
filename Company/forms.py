from django import forms
from BaseApp.models import User
from .models import CompanyModel


class CompanyRegisterForm(forms.Form):
    first_name = forms.CharField(
        label='نام',
        widget=forms.TextInput(attrs=
        {
            'class': 'form-control',
            'placeholder': 'نام'
        }),
    )

    last_name = forms.CharField(
        label='نام خانوادگی',
        widget=forms.TextInput(attrs=
        {
            'class': 'form-control',
            'placeholder': 'نام خانوادگی'
        }),
    )

    phone_number = forms.CharField(
        label='تلفن همراه',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'تلفن همراه'
        }),
    )

    email = forms.EmailField(
        label='پست الکترونیک',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'ایمیل'
        }),
    )

    number = forms.CharField(
        label='تلفن شرکت',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'تلفن شرکت'
        }),
    )

    company_name = forms.CharField(
        label='نام شرکت',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام شرکت'
        }),
    )

    numberـpersonnel = forms.CharField(
        label='تعداد پرسنل',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'تعداد پرسنل',
            'min': 1
        }),
    )

    address = forms.CharField(
        label='آدرس',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'آدرس'
        }),
    )


class UpdateCompanyProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام'
            }),

            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام خانوادگی'
            }),

            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ایمیل'
            }),

            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'تلفن همراه'
            }),

            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'آدرس'
            }),
        }

        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'email': 'ایمیل',
            'phone_number': 'شماره تلفن',
            'address': 'آدرس'
        }


class UpdateAdditionalCompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyModel
        fields = ['company_name', 'company_number', 'employee_count']

        widgets = {
            'company_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام شرکت',
            }),

            'company_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'تلفن شرکت'
            }),

            'employee_count': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'تعداد پرسنل'
            }),

        }

        labels = {
            'employee_name': 'نام شرکت',
            'employee_number': 'تلفن شرکت',
            'employee_count': 'تعداد پرسنل',
        }

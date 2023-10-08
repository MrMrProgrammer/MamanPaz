from django import forms
from BaseApp.models import User


class CustomerRegisterForm(forms.Form):
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
        widget=forms.TextInput(attrs={
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

    address = forms.CharField(
        label='آدرس',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'آدرس'
        }),
    )


class UpdateUserProfileForm(forms.ModelForm):
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

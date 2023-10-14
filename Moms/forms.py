from django import forms
from BaseApp.models import User
from .models import MomsModel


class MomRegisterForm(forms.Form):
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

    email = forms.EmailField(
        label='پست الکترونیک',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'ایمیل'
        }),
    )

    phone_number = forms.CharField(
        label='تلفن همراه',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'تلفن همراه'
        }),
    )

    address = forms.CharField(
        label='آدرس',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'آدرس'
        }),
    )


class UpdateMomProfileForm(forms.ModelForm):
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


class UpdateAdditionalMomProfileForm(forms.ModelForm):
    class Meta:
        model = MomsModel
        fields = ['profile_photo', 'home_number', 'state', 'city']

        widgets = {
            'profile_photo': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'عکس پروفایل',
                # 'placeholder': '',
            }),

            'home_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'تلفن ثابت'
            }),

            'state': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'استان'
            }),

            'city': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'شهر'
            }),

        }

        labels = {
            'profile_photo': 'عکس پروفایل',
            'home_number': 'تلفن ثابت',
            'state': 'استان',
            'city': 'شهر',
        }
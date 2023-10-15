from django import forms


class CompanyRegisterForm(forms.Form):

    name = forms.CharField(
        label='نام',
        widget=forms.TextInput(attrs=
        {
            'class': 'form-control',
            'placeholder': 'نام'
        }),
    )

    phone_number = forms.CharField(
        label='تلفن همراه',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'تلفن همراه'
        }),
    )

    number = forms.CharField(
        label='تلفن',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'تلفن'
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
            'placeholder': 'تعداد پرسنل'
        }),
    )

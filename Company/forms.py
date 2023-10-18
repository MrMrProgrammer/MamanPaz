from django import forms


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
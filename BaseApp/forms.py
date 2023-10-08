from django import forms


class LoginForm(forms.Form):
    email = forms.CharField(
        label='ایمیل',
        widget=forms.TextInput(attrs=
        {
            'class': 'form-control',
            'placeholder': 'ایمیل'
        }),
    )

    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'رمز عبور'
        }),
    )

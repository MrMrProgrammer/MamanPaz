from django import forms
from .models import FoodsModel


class AddFoodForm(forms.Form):
    is_active = forms.BooleanField(required=False, label='فعال / غیرفعال')

    food_name = forms.CharField(
        label='نام غذا',
        widget=forms.TextInput(attrs=
        {
            'class': 'form-control',
            'placeholder': 'نام غذا'
        }),
    )

    food_price = forms.IntegerField(
        label='قیمت غذا',
        widget=forms.NumberInput(attrs=
        {
            'class': 'form-control',
            'placeholder': 'قیمت غذا'
        }),
    )

    food_recipe = forms.CharField(
        label='دستور پخت',
        widget=forms.TextInput(attrs=
        {
            'class': 'form-control',
            'placeholder': 'دستور پخت'
        }),
    )

    food_photo = forms.ImageField(
        label='عکس غذا',
        widget=forms.ClearableFileInput(attrs=
        {
            'class': 'form-control',
            'placeholder': 'عکس غذا'
        }),
    )

    # raw_material = forms.ModelChoiceField(
    #     queryset=RawMaterial.objects.all(), empty_label=None,
    #
    #     label='مواد اولیه',
    #     widget=forms.SelectMultiple(attrs=
    #     {
    #         'class': 'form-control',
    #         'placeholder': 'مواد اولیه',
    #     }),
    # )


class UpdateFoodForm(forms.ModelForm):
    is_active = forms.BooleanField(required=False, label='فعال / غیرفعال')
    food_photo = forms.ImageField(required=False, widget=forms.FileInput)

    class Meta:
        model = FoodsModel
        fields = ['food_photo', 'food_name', 'food_price', 'food_recipe', 'is_active']

        widgets = {

            'food_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام غذا'
            }),
            'food_price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'قیمت'
            }),
            'food_recipe': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'دستورپخت'
            }),

            'food_photo': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'عکس غذا',

            }),
        }

        labels = {
            'food_name': 'نام غذا',
            'food_price': 'قیمت',
            'food_recipe': 'دستورپخت',
            'is_active': 'فعال / غیرفعال',
            'food_photo': 'عکس غذا'
        }

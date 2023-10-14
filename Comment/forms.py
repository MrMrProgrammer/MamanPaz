from django import forms
from .models import Comment, UserExperience


class CommentForm(forms.Form):
    user_experience = forms.ModelChoiceField(
        queryset=UserExperience.objects.all(),
        empty_label=None,
        widget=forms.RadioSelect,
    )

    text = forms.CharField(
        label='نظر',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'متن نظر شما',
            'rows': 3,
        }),
    )

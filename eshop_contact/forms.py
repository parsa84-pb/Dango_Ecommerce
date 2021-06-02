import re

from django import forms
from django.core import validators
from captcha.fields import ReCaptchaV3, ReCaptchaField


class CreateContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام و نام خانوادگی خود را وارد کنید', 'class': 'form-control'}),
        label='نام و نام خانوادگی',
        validators=[validators.MaxLengthValidator(150, 'نام و نام خانوادگی شما نمی تواند بیشتر از 150 کاراکتر باشد')])

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'ایمیل خود را وارد کنید', 'class': 'form-control', 'id': 'email'}),
        label='ایمیل',
        validators=[validators.MaxLengthValidator(150, 'ایمیل شما نمی تواند بیشتر از 150 کاراکتر باشد')])

    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'موضوع پیام خود را وارد کنید', 'class': 'form-control'}),
        label='موضوع',
        validators=[validators.MaxLengthValidator(150, 'موضوع پیام شما نمی تواند بیشتر از 150 کاراکتر باشد')])

    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'پیام خود را وارد کنید', 'class': 'form-control'}),
        label='پیام')
    captcha = ReCaptchaField(
        label="تصویر امنیتی",
        widget=ReCaptchaV3(api_params={'hl': "fa"}),
        error_messages={"required": 'لطفا تصویر امنیتی را کامل کنید'}
    )

    def clean_email(self):

        email = self.cleaned_data.get('email')
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

        if not re.search(regex, email):
            raise forms.ValidationError('ایمیل به درستی وارد نشده است')
        return email

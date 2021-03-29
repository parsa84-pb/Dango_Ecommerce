from django import forms
from django.core import validators


class UserNewOrderForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput())
    count = forms.IntegerField(widget=forms.NumberInput(), initial=1, min_value=1)


class UserInfo(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام و نام خانوادگی خود را وارد کنید', 'class': 'form-control'}),
        label='نام و نام خانوادگی',
        validators=[validators.MaxLengthValidator(150, 'نام و نام خانوادگی شما نمی تواند بیشتر از 150 کاراکتر باشد')])
    number = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'شماره همراه خود را وارد کنید', 'class': 'form-control'}),
        label='شماره همراه')
    address = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'آدرس خود را وارد کنید', 'class': 'form-control'}),
        label='آدرس',
        validators=[validators.MaxLengthValidator(1500, 'آدرس شما نمی تواند بیشتر از 1500 کاراکتر باشد')])
    postal_code = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': 'کد پستی خود را وارد کنید', 'class': 'form-control'}),
        label='کد پستی')


class ShowUserInfo(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'نام و نام خانوادگی خود را وارد کنید', 'class': 'form-control', 'disabled': 'True'}),
        label='نام و نام خانوادگی')
    number = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'شماره همراه خود را وارد کنید', 'class': 'form-control', 'disabled': 'True'}),
        label='شماره همراه')
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'آدرس خود را وارد کنید', 'class': 'form-control', 'disabled': 'True'}),
        label='آدرس')
    postal_code = forms.CharField(
        widget=forms.NumberInput(
            attrs={'placeholder': 'کد پستی خود را وارد کنید', 'class': 'form-control', 'disabled': 'True'}),
        label='کد پستی')

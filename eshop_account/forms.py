import re
from django import forms
from django.contrib.auth.models import User
from django.core import validators
from captcha.fields import ReCaptchaV3, ReCaptchaField


class EditUserProfile(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام خود را وارد کنید', 'class': 'form-control'}),
        label='نام کاربری')
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام خانوادگی خود را وارد کنید', 'class': 'form-control'}),
        label='نام کاربری')


class ShowUserProfile(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'نام خود را وارد کنید', 'disabled': 'True', 'class': 'form-control'}),
        label='نام کاربری')
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'نام خانوادگی خود را وارد کنید', 'disabled': 'True', 'class': 'form-control'}),
        label='نام کاربری')


class LoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری خود را وارد کنید'}),
        label='نام کاربری')
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور خود را وارد کنید'}),
        label='رمز عبور')
    captcha = ReCaptchaField(
        label="تصویر امنیتی",
        widget=ReCaptchaV3(api_params={'hl': "fa"}),
        error_messages={"required": 'لطفا تصویر امنیتی را کامل کنید'}
    )


class Register(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری خود را وارد کنید'}),
        label='نام کاربری',
        validators=[validators.MinLengthValidator(3, 'گلمه عبور نمی تواند کمتر از سه کاراکتر باشد')]
    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'placeholder': 'ایمیل خود را وارد کنید'}),
        label='ایمیل',
        validators=[validators.EmailValidator('ایمیل وارد شده معتبر نمی باشد')])
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور خود را وارد کنید'}),
        label='رمز عبور')
    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور خور را دوباره وارد کنید '}),
        label='تکرار رمز عبور')
    captcha = ReCaptchaField(
        label="تصویر امنیتی",
        widget=ReCaptchaV3(api_params={'hl': "fa"}),
        error_messages={"required": 'لطفا تصویر امنیتی را کامل کنید'}
    )

    def clean_email(self):

        user_name = self.cleaned_data.get('user_name')
        email = self.cleaned_data.get('email')

        user = User.objects.filter(username=user_name).exists()
        user2 = User.objects.filter(email=email).exists()

        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

        if user or user2:
            raise forms.ValidationError('شخص دیگری با این مشخصات ثبت نام کرده است ')
        elif not re.search(regex, email):
            raise forms.ValidationError('ایمیل به درستی وارد نشده است')
        return user_name

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')

        if password != re_password:
            raise forms.ValidationError('کلمه های عبور باهم مغایرت دارند')
        return password

# class ForgotPasswordGetEmailForm(forms.Form):
#     email = forms.EmailField(
#         widget=forms.EmailInput(attrs={'placeholder': 'ایمیل خود را وارد کنید:', 'class': 'form-control'}),
#         label='ایمیل')

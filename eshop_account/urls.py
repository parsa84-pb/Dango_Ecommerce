from django.urls import path
from django.contrib.auth import views as auth_views
from eshop_account.views import login_user, register, logout_user, user_account_main_page, edit_user_profile

urlpatterns = [
    path('login', login_user),
    path('register', register),
    path('logout_user', logout_user),
    path('user', user_account_main_page),
    path('user/edit', edit_user_profile),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'),
         name="reset_password"),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name="account/password_reset_done.html"),
         name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset_confirm.html"),
         name="password_reset_confirm"),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="account/password_reset_complete.html"),
         name="password_reset_complete"),
]

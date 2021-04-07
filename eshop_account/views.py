from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, Register, EditUserProfile, ShowUserProfile
from eshop_chat.models import Chat


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        user_name = login_form.cleaned_data.get('user_name')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=user_name, password=password)
        # if user is None:
        #     user = authenticate(request, email=user_name_or_gmail, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            login_form.add_error('user_name', 'کاربری با مشخصات وارد شده یافت نشد')

    context = {'login_form': login_form}
    return render(request, 'account/login.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    register_form = Register(request.POST or None)
    if register_form.is_valid():
        user_name = register_form.cleaned_data.get('user_name')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        user = User.objects.create_user(user_name, email, password)
        new_chat = Chat.objects.create(roomname=user_name)
        new_chat.members.add(user)
        new_chat.save()
        admins = User.objects.filter(is_superuser=True).all()
        for admin in admins:
            new_chat.members.add(admin)
            new_chat.save()

        return redirect('/login')

    context = {'register_form': register_form}
    return render(request, 'account/register.html', context)


def logout_user(request):
    logout(request)
    return redirect('/')


def user_account_main_page(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    if user is None:
        raise Http404()
    show_user_form = ShowUserProfile(request.POST or None,
                                     initial={'first_name': user.first_name, 'last_name': user.last_name})
    context = {'show_form': show_user_form}
    return render(request, 'account/user_account_main.html', context)


def edit_user_profile(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    if user is None:
        raise Http404()
    edit_user_form = EditUserProfile(request.POST or None,
                                     initial={'first_name': user.first_name, 'last_name': user.last_name})
    if edit_user_form.is_valid():
        first_name = edit_user_form.cleaned_data.get('first_name')
        last_name = edit_user_form.cleaned_data.get('last_name')
        user.first_name = first_name
        user.last_name = last_name
        user.save()

    context = {'edit_form': edit_user_form}
    return render(request, 'account/edit_user_profile.html', context)


def user_sidebar(request):
    context = {}
    return render(request, 'account/user_sidebar_partial.html', context)

# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Permission
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm

from app_dashboard_normaluser.models import normaluser
from django.contrib.contenttypes.models import ContentType


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            # Permission
            # ctype = ContentType.objects.get(app_label='authentication',model='normaluser')
            # perm = Permission.objects.get(codename='can_use_normal',content_type=ctype)
            # print(perm)

            # uuuu = User.objects.all()
            # print(uuuu)

            if user is not None:
                login(request, user)
                print(user.is_superuser)
                # print(request.path)
                # 身分(1) : Super User
                if (user.is_superuser == True):
                    print(user, 'Super User')

                    return redirect("/adminuser/")
                # 身分(2) : Normal User
                elif (user.has_perm('authentication.can_use_normal') == True):
                    print(user, 'Normal User')
                    return redirect("/normaluser/dashboard/")
                # 身分(3) : Teacher User
                elif (user.has_perm('authentication.can_use_admin') == True):
                    print(user, 'Teacher User')
                    return redirect("/adminuser/")
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            # Permission
            ctype = ContentType.objects.get(app_label='authentication', model='normaluser')
            perm = Permission.objects.get(codename='can_use_normal', content_type=ctype)
            user.user_permissions.add(perm)
            authtouser = User.objects.get(username=username)
            normaluser.objects.create(author=authtouser)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


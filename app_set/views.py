from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import os,shutil
import json


# Create your views here.
@login_required(login_url='/login/')
def setpage_normaluser(request):
    # SideBar
    context = {}
    context['segment'] = 'set'
    context['guardtag'] = 'normaluser/guard/'
    context['aggressiontag'] = 'normaluser/aggression/'
    context['contracttag'] = 'normaluser/contract/'
    context['dashboardtag'] = 'normaluser/dashboard/'
    context['settag'] = 'normaluser/set/'

    context['username'] = request.user

    return render(request, "set_folder/setpage_normaluser.html", context=context)
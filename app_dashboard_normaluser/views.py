# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template

from app_dashboard_normaluser.models import normaluser,normalusercode,normalusercompletecode
from app_contract.models import Contract_AddedTable

from logic_package.logic_Class_package.comparemachine_otm import *

@login_required(login_url="/login/")
def index(request):
    context = {}
    context['segment'] = 'dashboard'
    context['slider'] = 'normaluser/normal/'
    context['guardtag'] = 'normaluser/guard/'
    context['aggressiontag'] = 'normaluser/aggression/'
    context['contracttag'] = 'normaluser/contract/'
    context['dashboardtag'] = 'normaluser/dashboard/'
    context['historytag'] = 'normaluser/history/'
    context['howtag'] = 'normaluser/how/'
    context['abouttag'] = 'normaluser/about/'
    context['settag'] = 'normaluser/set/'

    context['username'] = request.user

    userdata = normaluser.objects.get(author = request.user)
    context['userdata'] = userdata
    html_template = loader.get_template('dashboard/normaluser_dashboardpage.html')
    return HttpResponse(html_template.render(context, request))



@login_required(login_url="/login/")
def normalpages(request,slider):

   load_template = slider + '.html'
   context={}
   context['segment'] = 'dashboard'
   context['slider'] = 'normaluser/normal/'
   context['guardtag'] = 'normaluser/guard/'
   context['aggressiontag'] = 'normaluser/aggression/'
   context['contracttag'] = 'normaluser/contract/'
   context['dashboardtag'] = 'normaluser/dashboard/'
   context['historytag'] = 'normaluser/history/'
   context['howtag'] = 'normaluser/how/'
   context['abouttag'] = 'normaluser/about/'
   context['settag'] = 'normaluser/set/'

   context['username'] = request.user
   userdata = normaluser.objects.get(author = request.user)
   context['userdata'] = userdata
   return render(request, load_template,context=context)


@login_required(login_url="/login/")
def normalpages_history(request):

    context = {}
    context['segment'] = 'history'
    context['slider'] = 'normaluser/normal/'
    context['guardtag'] = 'normaluser/guard/'
    context['aggressiontag'] = 'normaluser/aggression/'
    context['contracttag'] = 'normaluser/contract/'
    context['dashboardtag'] = 'normaluser/dashboard/'
    context['historytag'] = 'normaluser/history/'
    context['howtag'] = 'normaluser/how/'
    context['abouttag'] = 'normaluser/about/'
    context['settag'] = 'normaluser/set/'

    context['username'] = request.user
    userdata = normaluser.objects.get(author=request.user)
    context['userdata'] = userdata


    # Contract Add
    # 得到該使用者的加入合約資料
    temp_contractadddata = Contract_AddedTable.objects.filter(author=request.user)
    # 計算資料數量
    temp_contractadddata_count = temp_contractadddata.count()
    # 取得最後5筆
    try:
        contractadddata = temp_contractadddata[temp_contractadddata_count-5:temp_contractadddata_count]
    except:
        contractadddata = temp_contractadddata
    context['contractadddata'] = contractadddata

    # Contract Submit
    # 得到該使用者的上傳的合約資料
    temp_normalusersubmitdata = normalusercode.objects.filter(author=request.user)
    # 計算資料數量
    temp_normalusersubmitdata_count = temp_normalusersubmitdata.count()
    # 取得最後5筆
    try:
        normalusersubmitdata = temp_normalusersubmitdata[temp_normalusersubmitdata_count - 5:temp_normalusersubmitdata_count]
    except:
        normalusersubmitdata = temp_normalusersubmitdata

    context['normalusersubmitdata'] = normalusersubmitdata

    # Contract Complete
    # 得到該使用者的完成的合約資料
    temp_normalusercompletedata = normalusercompletecode.objects.filter(author=request.user)
    # 計算資料數量
    temp_normalusercompletedata_count = temp_normalusercompletedata.count()
    # 取得最後5筆
    try:
        normalusercompletedata = temp_normalusercompletedata[temp_normalusercompletedata_count - 5:temp_normalusercompletedata_count]
    except:
        normalusercompletedata = temp_normalusercompletedata
    context['normalusercompletedata'] = normalusercompletedata

    # Contract Compare Complete Code
    codecomparemachine = Comparetestmachine_otm(str(request.user),normalusercompletedata)
    temp_comparecodeexist = codecomparemachine.do_compare()
    comparecodeexist = temp_comparecodeexist
    context['comparecodeexist'] = comparecodeexist


    html_template = loader.get_template('information/normalhistory.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def normalpages_how(request):

    context = {}
    context['segment'] = 'how'
    context['slider'] = 'normaluser/normal/'
    context['guardtag'] = 'normaluser/guard/'
    context['aggressiontag'] = 'normaluser/aggression/'
    context['contracttag'] = 'normaluser/contract/'
    context['dashboardtag'] = 'normaluser/dashboard/'
    context['historytag'] = 'normaluser/history/'
    context['howtag'] = 'normaluser/how/'
    context['abouttag'] = 'normaluser/about/'
    context['settag'] = 'normaluser/set/'

    html_template = loader.get_template('information/how.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def normalpages_about(request):

    context = {}
    context['segment'] = 'about'
    context['slider'] = 'normaluser/normal/'
    context['guardtag'] = 'normaluser/guard/'
    context['aggressiontag'] = 'normaluser/aggression/'
    context['contracttag'] = 'normaluser/contract/'
    context['dashboardtag'] = 'normaluser/dashboard/'
    context['historytag'] = 'normaluser/history/'
    context['howtag'] = 'normaluser/how/'
    context['abouttag'] = 'normaluser/about/'
    context['settag'] = 'normaluser/set/'

    html_template = loader.get_template('information/about.html')
    return HttpResponse(html_template.render(context, request))
from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required



# Create your views here.
# Complete(Normal User)
@login_required(login_url='/login/')
def completepage_normaluser(request):
    # SideBar
    temp_context = {}
    temp_context['guardtag'] = 'normaluser/guard/'
    temp_context['aggressiontag'] = 'normaluser/aggression/'
    temp_context['contracttag'] = 'normaluser/contract/'
    temp_context['dashboardtag'] = 'normaluser/dashboard/'
    temp_context['settag'] = 'normaluser/set/'



    return render(request,"complete/completepages_normaluser.html",context=temp_context)
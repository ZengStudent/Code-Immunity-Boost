# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app_dashboard_normaluser import views as normaluser


urlpatterns = [

    # The home page
    path('', normaluser.index, name='home'),
    # History Page
    path('history/',normaluser.normalpages_history),
    # How Page
    path('how/', normaluser.normalpages_how),
    # About Page
    path('about/', normaluser.normalpages_about),

    # Matches any html file
    path('normal/<str:slider>/', normaluser.normalpages, name='pages'),


]

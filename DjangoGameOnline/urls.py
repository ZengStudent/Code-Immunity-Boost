# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("authentication.urls")), # Auth routes - login / register

    path("normaluser/", include("app_dashboard_normaluser.urls")),             # UI Kits Html files
    path("normaluser/guard/",include("app_guard.urls")),
    path("normaluser/aggression/",include("app_aggression.urls")),
    path("normaluser/contract/",include("app_contract.urls")),
    path("normaluser/dashboard/",include("app_dashboard_normaluser.urls")),
    path("normaluser/set/",include("app_set.urls")),
    path("normaluser/complete/",include("app_complete.urls")),

    path("adminuser/",include("app_dashboard_adminuser.urls")),
]

from django.urls import path
from . import views  #引用這個資料夾中的views檔案



urlpatterns = [
    # 未指定 Contract id
    #path('guardpage/', views.guard_otm),

    # Guard，One to Many
    path('guardotm/<contractid>', views.guard_otm),
    # Guard，Many to Many
    path('guardmtm/<contractid>', views.guard_mtm),
    # Guard，Many to One
    path('guardmto/<contractid>', views.guard_mto),
]
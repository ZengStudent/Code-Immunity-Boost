# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import  normaluser,normalusercode,normalusercompletecode,normalusercomplete_list


# NormalUser
class NormalUserAdmin(admin.ModelAdmin):
    list_display = ('author',)
    pass

# normalusercode
class NormalUserCodeAdmin(admin.ModelAdmin):
    list_display = ('id','author','contract_id','editorcode_submittime')
    pass

# normalusercompletecode
class NormalUserCompleteCodeAdmin(admin.ModelAdmin):
    list_display = ('id','author','contract_id','editorcode_completedtime','editorcode_isbasic','editorcode_isadvance')
    pass

# normalusercompletecode
class NormalUserCompleteListAdmin(admin.ModelAdmin):
    list_display = ('id','author','contract_id','editorcode_completedtime','editorcode_isbasic','editorcode_isadvance','complete_score','complete_rank')
    pass

# Register your models here.
admin.site.register(normaluser,NormalUserAdmin)
admin.site.register(normalusercode,NormalUserCodeAdmin)
admin.site.register(normalusercompletecode,NormalUserCompleteCodeAdmin)
admin.site.register(normalusercomplete_list,NormalUserCompleteListAdmin)










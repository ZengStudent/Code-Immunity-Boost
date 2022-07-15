from django.contrib import admin
from .models import Contract_Content,Contract_Perfect,Contract_Award,Contract,ContractInstance,Contract_AddedTable,Contract_CompletedTable

# Register your models here.


# Contract_Content
class Contract_ContentAdmin(admin.ModelAdmin):
    list_display = ('id','content_description','content_category','content_precent')
    pass
# Contract_Restrict
class Contract_PerfectAdmin(admin.ModelAdmin):
    list_display = ('id', 'perfect_description', 'perfect_category', 'perfect_precent')
    pass
# Contract_Award
class Contract_AwardAdmin(admin.ModelAdmin):
    list_display = ('id', 'award_basic', 'award_test', 'award_mutant')
    pass
# Contract
class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'tilte', 'contract_category', 'contract_mode')
    pass
# ContractInstance
class ContractInstanceAdmin(admin.ModelAdmin):
    list_display = ('id','contract')
    pass
# Contract_AddTable
class Contract_AddTableAdmin(admin.ModelAdmin):
    list_display = ('id','contract_id','author','addedtime',)
    pass
# Contract_CompleteTable
class Contract_CompleteTableAdmin(admin.ModelAdmin):
    list_display = ('id','contract_id','author','completedtime','complete_isbasic','complete_isadvance')
    pass



admin.site.register(Contract_Content,Contract_ContentAdmin)
admin.site.register(Contract_Perfect,Contract_PerfectAdmin)
admin.site.register(Contract_Award,Contract_AwardAdmin)
admin.site.register(Contract,ContractAdmin)
admin.site.register(ContractInstance,ContractInstanceAdmin)
admin.site.register(Contract_AddedTable,Contract_AddTableAdmin)
admin.site.register(Contract_CompletedTable,Contract_CompleteTableAdmin)















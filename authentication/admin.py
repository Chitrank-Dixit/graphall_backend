from django.contrib import admin
from authentication.models import Client, MasterAdmin


class ClientAdmin(admin.ModelAdmin):
    list_display = ['address', 'mobile_phone']
    list_filter = ['address', 'mobile_phone']
    search_fields = ['address', 'mobile_phone']

admin.site.register(Client, ClientAdmin)


class MasterAdminAdmin(admin.ModelAdmin):
    list_display = ['address', 'mobile_phone']
    list_filter = ['address', 'mobile_phone']
    search_fields = ['address', 'mobile_phone']

admin.site.register(MasterAdmin, MasterAdminAdmin)

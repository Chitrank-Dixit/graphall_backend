from django.contrib import admin
from authentication.models import Client, MasterAdmin


class ClientAdmin(admin.ModelAdmin):
    list_display = ['address', 'phone_number']
    list_filter = ['address', 'phone_number']
    search_fields = ['address', 'phone_number']

admin.site.register(Client, ClientAdmin)


class MasterAdminAdmin(admin.ModelAdmin):
    list_display = ['address', 'phone_number']
    list_filter = ['address', 'phone_number']
    search_fields = ['address', 'phone_number']

admin.site.register(MasterAdmin, MasterAdminAdmin)

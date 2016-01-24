from django.contrib import admin
from models import Client, MasterAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ClientResource(resources.ModelResource):

    class Meta:
        model = Client

class ClientAdmin(ImportExportModelAdmin):
    list_display = ['get_user_name','address', 'phone_number']
    list_filter = ['user__username','address', 'phone_number']
    search_fields = ['user__username','address', 'phone_number']
    resource_class = ClientResource

admin.site.register(Client, ClientAdmin)


class MasterAdminResource(resources.ModelResource):

    class Meta:
        model = MasterAdmin

class MasterAdminAdmin(ImportExportModelAdmin):
    list_display = ['get_user_name','address', 'phone_number']
    list_filter = ['user__username','address', 'phone_number']
    search_fields = ['user__username','address', 'phone_number']
    resource_class = MasterAdminResource

admin.site.register(MasterAdmin, MasterAdminAdmin)

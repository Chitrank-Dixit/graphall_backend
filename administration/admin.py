from django.contrib import admin
from administration.models import Plan
# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class PlanResource(resources.ModelResource):

    class Meta:
        model = Plan

class PlanAdmin(ImportExportModelAdmin):
    list_display = ['name', 'creation_time', 'deletion_time']
    list_filter = ['name', 'creation_time', 'deletion_time']
    search_fields = ['name', 'creation_time', 'deletion_time']
    resource_class = PlanResource

admin.site.register(Plan, PlanAdmin)


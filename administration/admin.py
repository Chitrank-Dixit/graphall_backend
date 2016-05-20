from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from models import Plan


class PlanResource(resources.ModelResource):

    class Meta:
        model = Plan

class PlanAdmin(ImportExportModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']
    resource_class = PlanResource

admin.site.register(Plan, PlanAdmin)


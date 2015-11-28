from django.contrib import admin
from administration.models import Plan
# Register your models here.


class PlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'creation_time', 'deletion_time']
    list_filter = ['name', 'creation_time', 'deletion_time']
    search_fields = ['name', 'creation_time', 'deletion_time']

admin.site.register(Plan, PlanAdmin)

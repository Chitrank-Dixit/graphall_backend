from django.contrib import admin

from django.contrib import admin
from analytics.models import TrackingSource, TrackingSourceDetails
# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class TrackingSourceResource(resources.ModelResource):

    class Meta:
        model = TrackingSource

class TrackingSourceAdmin(ImportExportModelAdmin):
    list_display = ['tracking_id','name','website', 'industry_category' ,'creation_time', 'deletion_time', 'is_active']
    list_filter = ['tracking_id','name','website', 'industry_category' ,'creation_time', 'deletion_time', 'is_active']
    search_fields = ['tracking_id','name','website', 'industry_category' ,'creation_time', 'deletion_time', 'is_active']
    resource_class = TrackingSourceResource

admin.site.register(TrackingSource, TrackingSourceAdmin)


class TrackingSourceDetailsResource(resources.ModelResource):

    class Meta:
        model = TrackingSourceDetails

class TrackingSourceDetailsAdmin(ImportExportModelAdmin):
    list_display = ['page_url','page_views','page_clicks','creation_time', 'deletion_time', 'is_active']
    list_filter = ['page_url','page_views','page_clicks','creation_time', 'deletion_time', 'is_active']
    search_fields = ['page_url','page_views','page_clicks','creation_time', 'deletion_time', 'is_active']
    resource_class = TrackingSourceDetailsResource

admin.site.register(TrackingSourceDetails, TrackingSourceDetailsAdmin)

from django.contrib import admin

from django.contrib import admin
from analytics.models import Tag, TrackingSource, TrackingSourceDetailsLog, TrackingSourceDetailsDaily, TrackingSourceDetailsWeekly, TrackingSourceDetailsMonthly, TrackingSourceDetailsYearly
# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class TagResource(resources.ModelResource):

    class Meta:
        model = Tag

class TagAdmin(ImportExportModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']
    resource_class = TagResource

admin.site.register(Tag, TagAdmin)


class TrackingSourceResource(resources.ModelResource):

    class Meta:
        model = TrackingSource

class TrackingSourceAdmin(ImportExportModelAdmin):
    list_display = ['tracking_id','name','website', 'industry_category' ,'creation_time', 'deletion_time', 'is_active','get_tag_details']
    list_filter = ['tracking_id','name','website', 'industry_category' ,'creation_time', 'deletion_time', 'is_active', 'tag__name']
    search_fields = ['tracking_id','name','website', 'industry_category' ,'creation_time', 'deletion_time', 'is_active', 'tag__name']
    resource_class = TrackingSourceResource

admin.site.register(TrackingSource, TrackingSourceAdmin)


class TrackingSourceDetailsLogResource(resources.ModelResource):

    class Meta:
        model = TrackingSourceDetailsLog

class TrackingSourceDetailsLogAdmin(ImportExportModelAdmin):
    list_display = ['get_tracking_source_tracking_id','get_tracking_source_name','page_url','page_views','page_clicks','creation_time', 'deletion_time', 'is_active']
    list_filter = ['tracking_source__tracking_id','tracking_source__name','page_url','page_views','page_clicks','creation_time', 'deletion_time', 'is_active']
    search_fields = ['tracking_source__tracking_id','tracking_source__name','page_url','page_views','page_clicks','creation_time', 'deletion_time', 'is_active']
    resource_class = TrackingSourceDetailsLogResource

admin.site.register(TrackingSourceDetailsLog, TrackingSourceDetailsLogAdmin)


class TrackingSourceDetailsDailyResource(resources.ModelResource):

    class Meta:
        model = TrackingSourceDetailsDaily

class TrackingSourceDetailsDailyAdmin(ImportExportModelAdmin):
    list_display = ['page_url','page_views','page_clicks','day' ,'creation_time', 'deletion_time', 'is_active']
    list_filter = ['page_url','page_views','page_clicks','day','creation_time', 'deletion_time', 'is_active']
    search_fields = ['page_url','page_views','page_clicks','day','creation_time', 'deletion_time', 'is_active']
    resource_class = TrackingSourceDetailsDailyResource

admin.site.register(TrackingSourceDetailsDaily, TrackingSourceDetailsDailyAdmin)


class TrackingSourceDetailsWeeklyResource(resources.ModelResource):

    class Meta:
        model = TrackingSourceDetailsWeekly

class TrackingSourceDetailsWeeklyAdmin(ImportExportModelAdmin):
    list_display = ['page_url','page_views','page_clicks','creation_time', 'deletion_time', 'is_active']
    list_filter = ['page_url','page_views','page_clicks','creation_time', 'deletion_time', 'is_active']
    search_fields = ['page_url','page_views','page_clicks','creation_time', 'deletion_time', 'is_active']
    resource_class = TrackingSourceDetailsWeeklyResource

admin.site.register(TrackingSourceDetailsWeekly, TrackingSourceDetailsWeeklyAdmin)


class TrackingSourceDetailsMonthlyResource(resources.ModelResource):

    class Meta:
        model = TrackingSourceDetailsMonthly

class TrackingSourceDetailsMonthlyAdmin(ImportExportModelAdmin):
    list_display = ['page_url','page_views','page_clicks','creation_time', 'month' ,'deletion_time', 'is_active']
    list_filter = ['page_url','page_views','page_clicks','creation_time', 'month','deletion_time', 'is_active']
    search_fields = ['page_url','page_views','page_clicks','creation_time', 'month' ,'deletion_time', 'is_active']
    resource_class = TrackingSourceDetailsMonthlyResource

admin.site.register(TrackingSourceDetailsMonthly, TrackingSourceDetailsMonthlyAdmin)


class TrackingSourceDetailsYearlyResource(resources.ModelResource):

    class Meta:
        model = TrackingSourceDetailsYearly

class TrackingSourceDetailsYearlyAdmin(ImportExportModelAdmin):
    list_display = ['page_url','page_views','page_clicks','creation_time' ,'deletion_time', 'is_active']
    list_filter = ['page_url','page_views','page_clicks','creation_time', 'deletion_time', 'is_active']
    search_fields = ['page_url','page_views','page_clicks','creation_time' ,'deletion_time', 'is_active']
    resource_class = TrackingSourceDetailsYearlyResource

admin.site.register(TrackingSourceDetailsYearly, TrackingSourceDetailsYearlyAdmin)



__author__ = 'chitrankdixit'
from django.conf.urls import patterns, url
from .views import track_source_details, get_custom_ranged_tracking_data

urlpatterns = patterns(
    'analytics.views',
)

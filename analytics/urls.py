__author__ = 'chitrankdixit'
from django.conf.urls import patterns, url
from .views import track_source_details, get_custom_ranged_tracking_data

urlpatterns = patterns(
    'analytics.views',

    # tracking page details from js script
    url(r'^tracking_source_details/$', track_source_details, name='track_page_details'),

    # get custom ranged data of the tracking source
    url(r'^get_custom_ranged_tracking_source_data/$', get_custom_ranged_tracking_data, name='custom_ranged_tracking_data'),
)

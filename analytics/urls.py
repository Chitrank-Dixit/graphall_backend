__author__ = 'chitrankdixit'
from django.conf.urls import patterns, url
from .views import track_source_details, get_custom_ranged_tracking_data, TrackingDataView

urlpatterns = patterns(
    'analytics.views',
    url(r'tracking_data/$', TrackingDataView.as_view(), name='trackingdata')
)

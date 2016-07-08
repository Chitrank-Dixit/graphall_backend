from django.conf.urls import patterns, url
from . import views
urlpatterns = patterns (
	'administration.views',
	url(r'plan-list/$', views.TestDjangoFilter.as_view(), name='plan_list')
)
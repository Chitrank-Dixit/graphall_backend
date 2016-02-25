"""graphall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework_nested import routers
from authentication.views import AccountViewSet, LoginView, LogoutView, ClientView, MasterAdminView
from administration.views import PlanViewSet, PlansListView
from analytics.views import TrackingSourceView, TrackingSourceDetailsLogView, TrackingDataView ,track_source_details, get_custom_ranged_tracking_data
#from graphall.views import IndexView

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'clients', ClientView)
router.register(r'masteradmins', MasterAdminView)
router.register(r'plans', PlanViewSet)
router.register(r'tracking_source', TrackingSourceView)
router.register(r'tracking_source_details_log', TrackingSourceDetailsLogView)

accounts_router = routers.NestedSimpleRouter(
    router, r'accounts', lookup='account'
)
clients_router = routers.NestedSimpleRouter(
    router, r'clients', lookup='client'
)
masteradmins_router = routers.NestedSimpleRouter(
    router, r'masteradmins', lookup='masteradmin'
)

plans_router = routers.NestedSimpleRouter(
    router, r'plans', lookup='plan'
)

tracking_source_router = routers.NestedSimpleRouter(
    router, r'tracking_source', lookup='tracking_source'
)

tracking_source_details_log_router = routers.NestedSimpleRouter(
    router, r'tracking_source_details_log', lookup='tracking_source_details_log'
)

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),  # JSON Web Tokens
    url(r'^api-token-refresh/', 'rest_framework_jwt.views.refresh_jwt_token'),  # JSON Web Tokens
    url(r'^api-token-verify/', 'rest_framework_jwt.views.verify_jwt_token'),  # JSON Web Tokens
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/', include(accounts_router.urls)),
    url(r'^api/v1/', include(clients_router.urls)),
    url(r'^api/v1/', include(masteradmins_router.urls)),
    url(r'^api/v1/', include(plans_router.urls)),
    url(r'^api/v1/', include(tracking_source_router.urls)),
    url(r'^api/v1/', include(tracking_source_details_log_router.urls)),


    url(r'^api/v1/plan/list/$', PlansListView.as_view(), name='planlist'),
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),
    #url('^.*$', IndexView.as_view(), name='index'),

    url(r'^docs/', include('rest_framework_swagger.urls')),  # django rest swagger

    # tracking page details from js script
    url(r'^tracking_source_details/$', track_source_details, name='track_page_details'),

    # get custom ranged data of the tracking source
    url(r'^get_custom_ranged_tracking_source_data/$', get_custom_ranged_tracking_data, name='custom_ranged_tracking_data'),

    # get custom ranged data new API
    url(r'^api/v1/tracking_data/$', TrackingDataView.as_view(), name='trackingdata')



]

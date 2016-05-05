import json, random
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, viewsets, status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from models import TrackingSource, TrackingSourceDetailsLog, WebBrowser
from serializers import TrackingSourceSerializer, TrackingSourceDetailsLogSerializer
from utils import set_response_header, JsonResponse


class TrackingSourceView(viewsets.ModelViewSet):
    queryset = TrackingSource.objects.all()
    serializer_class = TrackingSourceSerializer


    # def get_permissions(self):
    #     if self.request.method in permissions.SAFE_METHODS:
    #         return (permissions.AllowAny(),)
    #     return (permissions.IsAuthenticated(), IsClientOfSite(),)

    def perform_create(self, serializer):
        tracking_id = 'GPAL-' + ''.join(
            [str(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')) for i in xrange(6)])
        instance = serializer.save(client=self.request.user.client, tracking_id=tracking_id)
        return super(TrackingSourceView, self).perform_create(serializer)


class TrackingSourceDetailsLogView(viewsets.ModelViewSet):
    queryset = TrackingSourceDetailsLog.objects.all()
    serializer_class = TrackingSourceDetailsLogSerializer


    # def get_permissions(self):
    #     if self.request.method in permissions.SAFE_METHODS:
    #         return (permissions.AllowAny(),)
    #     return (permissions.IsAuthenticated(), IsClientOfSite(),)

    # def perform_create(self, serializer):
    #     instance = serializer.save(user=self.request.user)
    #     return super(TrackingSourceDetailsView, self).perform_create(serializer)


class TrackingDataView(APIView):

    """
    API view to get the source details of the item.
    """


    def get(self, request, *args, **kwargs):
        """
        This is the filtered data based on tracking source and the date range supplied
        """
        response_json = {}
        page_clicks = 0
        page_views = 0
        web_browser = []
        tracking_data = TrackingSourceDetailsLog.objects.filter(tracking_source__tracking_id=str(request.query_params['tracking_source_id']))
        for item in tracking_data:
            page_clicks += item.page_clicks
            page_views += item.page_views
            web_browser.append(item.web_browser)

        response_json.update({"page_views": page_views, "page_clicks": page_clicks, "web_browser": web_browser})
        return Response(response_json)



@csrf_exempt
def track_source_details(request):
    """
        View to add all the tracking resources it can not be written with permissions as it is the data that would sent by the tracking script
    """

    status, response = set_response_header(request=request, response=HttpResponse(content_type='application/json'))
    if not status:
        return HttpResponseBadRequest(json.dumps({"Message": "Unauthorized request"}), content_type='application/json')
    params = json.loads(request.body)
    data = {'msg': 'unexpected behavior'}
    try:
        tracking_source = TrackingSource.objects.get(tracking_id=params['tracking_source'])
        params.update({'tracking_source': tracking_source})
        # # either get the existing page tracking record or if not found just create it
        # tracking_source_details = TrackingSourceDetailsLog.objects.get(page_url=str(params['page_url']))
        # if tracking_source_details:
        #     tracking_source_details.page_clicks = int(tracking_source_details.page_clicks) + int(params['page_clicks'])
        #     tracking_source_details.page_views = int(tracking_source_details.page_views) + int(params['page_views'])
        #     tracking_source_details.save()
        # data['msg'] = 'data updated'


        TrackingSourceDetailsLog.objects.create(**params)
        data['msg'] = 'data created'

    except Exception, e:
        pass
    response.write("%s" % (json.dumps(data)))
    return response


@csrf_exempt
def get_custom_ranged_tracking_data(request):
    """

    :param request:
    :return:

    """
    params = json.loads(request.body)
    response_json = {}
    page_clicks = 0
    page_views = 0
    web_browser = []
    tracking_data = TrackingSourceDetailsLog.objects.filter(tracking_source__tracking_id=params['tracking_source_id'])
    for item in tracking_data:
        page_clicks += item.page_clicks
        page_views += item.page_views
        web_browser.append(item.web_browser)

    response_json.update({"page_views": page_views, "page_clicks": page_clicks, "web_browser": web_browser})
    return JsonResponse(response_json)

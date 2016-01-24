import json
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, viewsets
from models import TrackingSource, TrackingSourceDetailsLog
from serializers import TrackingSourceSerializer, TrackingSourceDetailsLogSerializer
from utils import set_response_header

class TrackingSourceView(viewsets.ModelViewSet):


    queryset = TrackingSource.objects.all()
    serializer_class = TrackingSourceSerializer


    # def get_permissions(self):
    #     if self.request.method in permissions.SAFE_METHODS:
    #         return (permissions.AllowAny(),)
    #     return (permissions.IsAuthenticated(), IsClientOfSite(),)

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)
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

@csrf_exempt
def track_source_details(request):
    status,response = set_response_header(request=request,response=HttpResponse(content_type='application/json'))
    if not status:
        return HttpResponseBadRequest(json.dumps({"Message":"Unauthorized request"}),content_type='application/json')
    params = json.loads(request.body)
    data = {}
    data['msg'] = 'unexpected vehavior'
    try:
        tracking_source = TrackingSource.objects.get(tracking_id=params['tracking_source'])
        params.update({'tracking_source': tracking_source})
        # either get the existing page tracking record or if not found just create it
        tracking_source_details = TrackingSourceDetailsLog.objects.get(page_url=str(params['page_url']))
        if tracking_source_details:
            tracking_source_details.page_clicks = int(tracking_source_details.page_clicks) + int(params['page_clicks'])
            tracking_source_details.page_views = int(tracking_source_details.page_views) + int(params['page_views'])
            tracking_source_details.save()



        data['msg'] = 'data updated'
    except Exception, e:
        try:
            TrackingSourceDetailsLog.objects.create(**params)
            data['msg'] = 'data created'
        except Exception, e:
            data['msg'] = 'failed'

    response.write("%s"%(json.dumps(data)))
    return response



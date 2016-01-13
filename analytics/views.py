from django.shortcuts import render
from rest_framework import permissions, viewsets
from models import TrackingSource, TrackingSourceDetails
from serializers import TrackingSourceSerializer, TrackingSourceDetailsSerializer

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


class TrackingSourceDetailsView(viewsets.ModelViewSet):


    queryset = TrackingSourceDetails.objects.all()
    serializer_class = TrackingSourceDetailsSerializer


    # def get_permissions(self):
    #     if self.request.method in permissions.SAFE_METHODS:
    #         return (permissions.AllowAny(),)
    #     return (permissions.IsAuthenticated(), IsClientOfSite(),)

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)
        return super(TrackingSourceDetailsView, self).perform_create(serializer)
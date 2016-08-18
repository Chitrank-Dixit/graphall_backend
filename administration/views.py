from oauth2_provider.ext.rest_framework import OAuth2Authentication
from rest_framework import permissions, status, views, viewsets, filters
from rest_framework.generics import ListAPIView
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from administration.filters import PlanFilter
from administration.utils import TenItemsSetPagination
from models import Plan
from serializers import PlanSerializer


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (OAuth2Authentication, )


class PlansListView(ListAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    pagination_class = TenItemsSetPagination


class TestDjangoFilter(ListAPIView):
    serializer_class = PlanSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = PlanFilter

    def get_queryset(self):
        queryset = Plan.objects.all()
        return queryset
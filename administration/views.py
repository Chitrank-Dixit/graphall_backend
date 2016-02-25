from rest_framework import permissions, status, views, viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from administration.utils import TenItemsSetPagination
from models import Plan
from serializers import PlanSerializer


class PlanViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class PlansListView(ListAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    pagination_class = TenItemsSetPagination


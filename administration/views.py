import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework import permissions, status, views, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from administration.models import Plan
from administration.serializers import PlanSerializer
#from authentication.permissions import IsAccountOwner, IsAuthorOfPost
#from authentication.serializers import AccountSerializer


class PlanViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer





import django_filters
from rest_framework import filters
from rest_framework.filters import DjangoFilterBackend

from administration.models import Plan

__author__ = 'chitrankdixit'


class PlanFilter(filters.FilterSet, DjangoFilterBackend):
    name = django_filters.CharFilter(name="name", lookup_type="iexact")

    class Meta:
        model = Plan
        fields = ['name',]

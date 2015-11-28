from django.contrib.auth import update_session_auth_hash

from rest_framework import serializers

from django.contrib.auth.models import User
from administration.models import Plan
from authentication.serializers import ClientSerializer


class PlanSerializer(serializers.ModelSerializer):
    planwise_clients = ClientSerializer(many=True)
    class Meta:
        model = Plan
        fields = ('name', 'creation_time', 'deletion_time','planwise_clients')
from rest_framework import serializers
from authentication.serializers import ClientSerializer
from models import Plan



class PlanSerializer(serializers.ModelSerializer):
    planwise_clients = ClientSerializer(many=True)
    class Meta:
        model = Plan
        fields = ('name', 'creation_time', 'deletion_time','planwise_clients')
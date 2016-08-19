__author__ = 'chitrankdixit'
from rest_framework import serializers
from models import TrackingSource, TrackingSourceDetailsLog

class TrackingSourceSerializer(serializers.ModelSerializer):


    def get_validation_exclusions(self, *args, **kwargs):
        # Need to exclude `user` since we'll add that later based off the request
        exclusions = super(TrackingSourceSerializer, self).get_validation_exclusions(*args, **kwargs)
        return exclusions + ['user']

    class Meta:
        model = TrackingSource
        fields = ('tracking_id','name','website', 'industry_category' , 'is_active')


    def create(self, validated_data):
        self.initial_data['tracking_id'] = validated_data['tracking_id']
        return TrackingSource.objects.create(**validated_data)




    # def update(self, instance, validated_data):

    #     pass

    # def to_internal_value(self, data):
    #     pass
    #
    # def to_representation(self, value):
    #     pass


class TrackingSourceDetailsLogSerializer(serializers.ModelSerializer):


    # def get_validation_exclusions(self, *args, **kwargs):
    #     # Need to exclude `user` since we'll add that later based off the request
    #     exclusions = super(TrackingSourceDetailsSerializer, self).get_validation_exclusions(*args, **kwargs)
    #     return exclusions + ['user']

    class Meta:
        model = TrackingSourceDetailsLog
        fields = ('tracking_source','page_url','page_views','page_clicks','web_browser', 'is_active','a')
        depth = 1


    def create(self, validated_data):
        tracking_source_data = self.initial_data['tracking_source']
        tracking_source = TrackingSource.objects.get(tracking_id=tracking_source_data)
        validated_data['tracking_source'] = tracking_source
        return TrackingSourceDetailsLog.objects.create(**validated_data)

    # def create(self, validated_data):
    #     return MasterAdmin.objects.create(**validated_data)
    #     # obj.save(user_id=validated_data['user'])
    #     # return obj
    #
    # def update(self, instance, validated_data):
    #     pass

    # def to_internal_value(self, data):
    #     pass
    #
    # def to_representation(self, value):
    #     pass

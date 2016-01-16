__author__ = 'chitrankdixit'
from rest_framework import serializers
from models import TrackingSource, TrackingSourceDetails

class TrackingSourceSerializer(serializers.ModelSerializer):


    def get_validation_exclusions(self, *args, **kwargs):
        # Need to exclude `user` since we'll add that later based off the request
        exclusions = super(TrackingSourceSerializer, self).get_validation_exclusions(*args, **kwargs)
        return exclusions + ['user']

    class Meta:
        model = TrackingSource
        fields = ('tracking_id','name','website', 'industry_category' ,'creation_time', 'deletion_time', 'is_active')



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


class TrackingSourceDetailsSerializer(serializers.ModelSerializer):


    # def get_validation_exclusions(self, *args, **kwargs):
    #     # Need to exclude `user` since we'll add that later based off the request
    #     exclusions = super(TrackingSourceDetailsSerializer, self).get_validation_exclusions(*args, **kwargs)
    #     return exclusions + ['user']

    class Meta:
        model = TrackingSourceDetails
        fields = ('tracking_source','page_url','page_views','page_clicks','creation_time', 'deletion_time', 'is_active')
        depth = 1


    def create(self, validated_data):
        tracking_source_data = self.initial_data['tracking_source']
        tracking_source = TrackingSource.objects.get(tracking_id=tracking_source_data)
        validated_data['tracking_source'] = tracking_source
        return TrackingSourceDetails.objects.create(**validated_data)

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

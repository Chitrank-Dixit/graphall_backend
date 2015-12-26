from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers

from authentication.models import Client, MasterAdmin
from django.contrib.auth.models import User



class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    #confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'password', 'date_joined', 'last_login')
        read_only_fields = ('date_joined', 'last_login',)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        # instance.tagline = validated_data.get('tagline', instance.tagline)

        instance.save()

        password = validated_data.get('password', None)
        #confirm_password = validated_data.get('confirm_password', None)

        if password:
            instance.set_password(password)
            instance.save()

        update_session_auth_hash(self.context.get('request'), instance)

        return instance

    # def to_internal_value(self, data):
    #     pass
    #
    # def to_representation(self, value):
    #     pass


class ClientSerializer(serializers.ModelSerializer):
    user = AccountSerializer(required=False)

    def get_validation_exclusions(self, *args, **kwargs):
        # Need to exclude `user` since we'll add that later based off the request
        exclusions = super(ClientSerializer, self).get_validation_exclusions(*args, **kwargs)
        return exclusions + ['user']

    class Meta:
        model = Client
        fields = ('address', 'phone_number', 'user_type','plan', 'user')
        depth = 1  # increase the depth to navigate to mode detailed view in the api's

    # def create(self, validated_data):
    #     pass
    #
    # def update(self, instance, validated_data):
    #     pass

    # def to_internal_value(self, data):
    #     pass
    #
    # def to_representation(self, value):
    #     pass


class MasterAdminSerializer(serializers.ModelSerializer):
    user = AccountSerializer(required=False)

    def get_validation_exclusions(self, *args, **kwargs):
        # Need to exclude `user` since we'll add that later based off the request
        exclusions = super(MasterAdminSerializer, self).get_validation_exclusions(*args, **kwargs)
        return exclusions + ['user']

    class Meta:
        model = MasterAdmin
        fields = ('address', 'phone_number', 'user_type' , 'user')



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

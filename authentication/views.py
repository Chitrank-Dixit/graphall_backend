import json
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from oauth2_provider.ext.rest_framework import OAuth2Authentication
from oauth2_provider.models import AccessToken
from rest_framework import permissions, status, views, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_extensions.cache.decorators import (
    cache_response
)
from rest_framework_social_oauth2.views import ConvertTokenView
from social.apps.django_app.default.models import UserSocialAuth
from rest_framework import status
from rest_framework.response import Response
from social.apps.django_app.utils import load_backend
from social.backends.oauth import BaseOAuth1, BaseOAuth2
from social.exceptions import AuthAlreadyAssociated
from authentication.simple_encryption import SimpleEncryptionDecryption
from miscellaneous.mixins import CustomMetaDataMixin
from models import Client, MasterAdmin, UserType
from permissions import IsAccountOwner, IsMasterAdminOfSite, IsClientOfSite
from serializers import AccountSerializer, ClientSerializer, MasterAdminSerializer, SocialAccountSerializer


class AccountViewSet(CustomMetaDataMixin,viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AccountSerializer
    # authentication_classes = (JSONWebTokenAuthentication,)
    authentication_classes = (OAuth2Authentication, )
    permission_classes = (IsAuthenticated,)
    lookup_field = 'username'

    def get_queryset(self):
        if self.request.user.is_staff:
            return User.objects.all()
        return User.objects.filter(pk=self.request.user.id)

    def get_permissions(self):
        #permission_classes = (IsAuthenticated,)
        #authentication_classes = (JSONWebTokenAuthentication,)
        # if self.request.method in permissions.SAFE_METHODS:
        #     return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            User.objects.create_user(**serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)


class SocialAccountViewSet(CustomMetaDataMixin,viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SocialAccountSerializer
    # authentication_classes = (JSONWebTokenAuthentication,)
    authentication_classes = (OAuth2Authentication, )
    permission_classes = (IsAuthenticated,)
    lookup_field = 'username'

    def get_queryset(self):
        if self.request.user.is_staff:
            return User.objects.all()
        return User.objects.filter(pk=self.request.user.id)

    def get_permissions(self):
        #permission_classes = (IsAuthenticated,)
        #authentication_classes = (JSONWebTokenAuthentication,)
        # if self.request.method in permissions.SAFE_METHODS:
        #     return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):
        provider = request.data.pop('provider')
        uid = None
        if provider == 'facebook':
            uid = request.data.pop('fb_id')
        elif provider == 'google-plus':
            uid = request.data.get('email')
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(**serializer.validated_data)
            UserSocialAuth.objects.create(
                user_id = user.pk,
                provider = provider,
                uid = uid,
                extra_data = {}
            )
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)

class LoginView(CustomMetaDataMixin, views.APIView):
    queryset = User.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (OAuth2Authentication, )

    def post(self, request, format=None):
        username = request.data.get('username', None)#data.get('username', None)
        password = request.data.get('password', None)#data.get('password', None)
        account = authenticate(username=username, password=password)

        if account is not None:
            if account.is_active:
                login(request, account)
                serialized = self.serializer_class(account)
                return Response(serialized.data, status=status.HTTP_200_OK)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(CustomMetaDataMixin, views.APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (OAuth2Authentication, )
    #authentication_classes = (JSONWebTokenAuthentication,)

    def post(self, request, format=None):
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)


class ClientView(CustomMetaDataMixin, viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (OAuth2Authentication, )

    #@cache_response()
    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(), IsClientOfSite(),)

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)
        return super(ClientView, self).perform_create(serializer)


class MasterAdminView(CustomMetaDataMixin, viewsets.ModelViewSet):
    queryset = MasterAdmin.objects.all()
    serializer_class = MasterAdminSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (OAuth2Authentication, )

    #@cache_response()
    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(), IsMasterAdminOfSite(),)

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)
        return super(MasterAdminView, self).perform_create(serializer)


class CustomConvertTokenView(CustomMetaDataMixin, ConvertTokenView):
    """
        1. **authentication:** no
        2. **authorization:** Any

        **Suggested edits:**

        1. Details about user in response?
    """
    def post(self, request, *args, **kwargs):
        try:
            encrypted_client_secret = request.data['client_secret_web']
            request.data['client_secret'] = self.decrypt_client_secret(encrypted_client_secret)
        except KeyError:
            pass
        # is_new_user = True

        # user_social_auth = UserSocialAuth.objects.filter(uid=request.data['social_id'], provider=request.data['backend']).first()
        # if user_social_auth is not None and user_social_auth.user.proformainvoice_set.count() > 0:
        #     is_new_user = False
        #response = super(self, ConvertTokenView)
        response = super(CustomConvertTokenView, self).post(self, request, *args, **kwargs)

        try:
            user = AccessToken.objects.get(token=response.data['access_token']).user
            response.data['user_id'] = user.id
            response.data['email'] = user.email
            response.data['name'] = user.first_name + " " + user.last_name
        except KeyError:
            pass

        return response

    def decrypt_client_secret(self, encrypted_client_secret):
        return SimpleEncryptionDecryption.decrypt(encrypted_client_secret)



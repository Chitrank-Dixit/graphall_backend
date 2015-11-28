import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework import permissions, status, views, viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from authentication.models import Client, MasterAdmin
from authentication.permissions import IsAccountOwner
from authentication.serializers import AccountSerializer, ClientSerializer, MasterAdminSerializer


class AccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = User.objects.all()
    print queryset
    serializer_class = AccountSerializer
    #print "AccountSerializer mein aaa gaya", viewsets.ModelViewSet
    def get_permissions(self):
        #print "permissions mein aaa gaya", self.request.method, permissions.SAFE_METHODS
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            #print "In Post"
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):
        #print "create mein aaa gaya", self.serializer_class(data=request.data)," ji"
        serializer = self.serializer_class(data=request.data)
        print serializer
        if serializer.is_valid():
            print "users mein aa gaya"
            User.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        print request.data
        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)


class LoginView(views.APIView):

    queryset = User.objects.all()

    def post(self, request, format=None):
        data = json.loads(request.body)
        username = data.get('username', None)
        password = data.get('password', None)
        account = authenticate(username=username, password=password)

        if account is not None:
            if account.is_active:
                login(request, account)
                serialized = AccountSerializer(account)
                return Response(serialized.data)
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


class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)


class ClientView(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class MasterAdminView(viewsets.ModelViewSet):
    queryset = MasterAdmin.objects.all()
    serializer_class = MasterAdminSerializer
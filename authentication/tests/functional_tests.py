import json
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework_jwt import utils
from administration.models import Plan
from authentication.models import MasterAdmin, Client

__author__ = 'chitrankdixit'

# need to make user related test cases as well
# signup and signin user related test cases
# logout test case




class MasterAdminCreateTestCase(APITestCase):
    """
        This Test case would test for the Master Admin created in django
    """

    def setUp(self):
        """
        """
        self.csrf_client = APIClient(enforce_csrf_checks=True)
        self.user = User.objects.create(
            username='cristiano',
            password='ronaldo'
        )

    def master_admin_create(self):
        """
            This test case would create the master admin
        """
        payload = utils.jwt_payload_handler(self.user)
        token = utils.jwt_encode_handler(payload)
        response = self.client.post('/api/v1/masteradmins/', data={"user": self.user, "address": "Sudama Nagar Indore",
                                                                   "phone_number": "+919769730095", "user_type": "2"},
                                    HTTP_AUTHORIZATION="jwt " + str(token))
        self.assertEqual(response.status_code, 201)


class MasterAdminListDetailDeleteUpdateCase(APITestCase):
    """
        This is the test case to check the TrackingDataView API is working well or not
    """

    def setUp(self):
        """

        """
        self.csrf_client = APIClient(enforce_csrf_checks=True)
        self.user = User.objects.create(
            username='cristiano',
            password='ronaldo'
        )
        self.masteradmin = MasterAdmin.objects.create(
            user=self.user,
            registered_type=1,
            address="Sudama Nagar Indore",
            phone_number="+919769730095",
            user_type="2"
        )

    def get_master_admin_list(self):
        """
            Get List of all the Master Admin Registered
        """

        # response = self.client.get('')

        payload = utils.jwt_payload_handler(self.user)
        token = utils.jwt_encode_handler(payload)
        response = self.client.get('/api/v1/masteradmins/', HTTP_AUTHORIZATION="jwt " + str(token))
        self.assertEqual(response.status_code, 200)

    def get_master_admin_detail(self):
        """
            Get detail of a master admin user
        """
        payload = utils.jwt_payload_handler(self.user)
        token = utils.jwt_encode_handler(payload)
        response = self.client.get('/api/v1/masteradmins/' + str(self.masteradmin.id) + '/',
                                   HTTP_AUTHORIZATION="jwt " + str(token))
        self.assertEqual(response.status_code, 200)

    def delete_master_admin(self):
        """
            Delete the master admin
        """
        payload = utils.jwt_payload_handler(self.user)
        token = utils.jwt_encode_handler(payload)
        response = self.client.delete('/api/v1/masteradmins/' + str(self.masteradmin.id) + '/',
                                      HTTP_AUTHORIZATION="jwt " + str(token))
        self.assertEqual(response.status_code, 204)

    def update_master_admin(self):
        """
            update the master admin
        """
        payload = utils.jwt_payload_handler(self.user)
        token = utils.jwt_encode_handler(payload)
        response = self.client.put('/api/v1/masteradmins/' + str(self.masteradmin.id) + '/',
                                   data={"address": "Sudama Nagar Indore", "phone_number": "+919769730095",
                                         "user_type": "2"}, HTTP_AUTHORIZATION="jwt " + str(token))
        self.assertEqual(response.status_code, 200)

    def partial_update_master_admin(self):
        """
            partial update the master admin
        """
        payload = utils.jwt_payload_handler(self.user)
        token = utils.jwt_encode_handler(payload)
        response = self.client.patch('/api/v1/masteradmins/' + str(self.masteradmin.id) + '/',
                                     data={"address": "Sudama Nagar Indore"}, HTTP_AUTHORIZATION="jwt " + str(token))
        self.assertEqual(response.status_code, 200)


class ClientCreateTestCase(APITestCase):
    """
        This Test case would test for the Master Admin created in django
    """

    def setUp(self):
        """
        """
        self.csrf_client = APIClient(enforce_csrf_checks=True)
        self.user = User.objects.create(
            username='cristiano',
            password='ronaldo'
        )
        self.plan = Plan.objects.create(name="Demo")

    def client_create(self):
        """
            This test case would create the master admin
        """
        payload = utils.jwt_payload_handler(self.user)
        token = utils.jwt_encode_handler(payload)
        # "plan": self.plan.id cause django was expecting an id there and I was giving the plan instance
        response = self.client.post('/api/v1/clients/',
                                    data={"user": self.user, "plan": self.plan.id, "address": "Sudama Nagar Indore",
                                          "phone_number": "+919769730095", "user_type": "1"},
                                    HTTP_AUTHORIZATION="jwt " + str(token))
        self.assertEqual(response.status_code, 201)


class ClientListDetailDeleteUpdateCase(APITestCase):
    """
        This is the test case to check the TrackingDataView API is working well or not
    """

    def setUp(self):
        """

        """
        self.csrf_client = APIClient(enforce_csrf_checks=True)
        self.user = User.objects.create(
            username='cristiano',
            password='ronaldo'
        )
        self.plan = Plan.objects.create(name="Demo")
        self.clients = Client.objects.create(
            plan_id=self.plan.id,
            user=self.user,
            address="Sudama Nagar Indore",
            phone_number="+919769730095",
            user_type="1"
        )

    def get_client_list(self):
        """
            Get List of all the Master Admin Registered
        """

        # response = self.client.get('')

        payload = utils.jwt_payload_handler(self.user)
        token = utils.jwt_encode_handler(payload)
        response = self.client.get('/api/v1/clients/', HTTP_AUTHORIZATION="jwt " + str(token))
        self.assertEqual(response.status_code, 200)

    def get_client_detail(self):
        """
            Get detail of a master admin user
        """
        payload = utils.jwt_payload_handler(self.user)
        token = utils.jwt_encode_handler(payload)
        response = self.client.get('/api/v1/clients/' + str(self.clients.id) + '/',
                                   HTTP_AUTHORIZATION="jwt " + str(token))
        self.assertEqual(response.status_code, 200)

    def delete_client(self):
        """
            Delete the master admin
        """
        payload = utils.jwt_payload_handler(self.user)
        token = utils.jwt_encode_handler(payload)
        response = self.client.delete('/api/v1/clients/' + str(self.clients.id) + '/',
                                      HTTP_AUTHORIZATION="jwt " + str(token))
        self.assertEqual(response.status_code, 204)

    def update_client(self):
        """
            update the master admin
        """
        payload = utils.jwt_payload_handler(self.user)
        token = utils.jwt_encode_handler(payload)
        response = self.client.put('/api/v1/clients/' + str(self.clients.id) + '/',
                                   data={"user": self.user, "plan": self.plan.id, "address": "Sudama Nagar Indore", "phone_number": "+919769730095",
                                         "user_type": "2"}, HTTP_AUTHORIZATION="jwt " + str(token))
        self.assertEqual(response.status_code, 200)

    def partial_update_client(self):
        """
            partial update the master admin
        """
        payload = utils.jwt_payload_handler(self.user)
        token = utils.jwt_encode_handler(payload)
        response = self.client.patch('/api/v1/clients/' + str(self.clients.id) + '/',
                                     data={"plan": self.plan.id,"address": "Sudama Nagar Indore"}, HTTP_AUTHORIZATION="jwt " + str(token))
        self.assertEqual(response.status_code, 200)

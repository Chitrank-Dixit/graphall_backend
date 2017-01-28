from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework_jwt import utils
from administration.models import Plan


__author__ = 'chitrankdixit'


class PlanCreateTestCase(APITestCase):
    """
        This is the test case for the plan creation
    """
    def setUp(self):
        """
            Initial setup for creating test case
        """
        self.csrf_client = APIClient(enforce_csrf_checks=True)
        self.user = User.objects.create(
            username='cristiano',
            password='ronaldo'
        )

    def plan_create(self):
        """
            Test case to create plan
        """
        payload = utils.jwt_payload_handler(self.user)
        token = utils.jwt_encode_handler(payload)
        response = self.client.post('/api/v1/plans/', data={"name": "Demo Create", "planwise_clients": self.user},
                                    HTTP_AUTHORIZATION="jwt " + str(token))
        self.assertEqual(response.status_code, 201)


class PlanListDetailDeleteUpdateTestCase(APITestCase):
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
        self.plan = Plan.objects.create(
            name='Demo'
        )

    def test_get_plan_list(self):
        """
            Get List of all the Master Admin Registered
        """
        payload = utils.jwt_payload_handler(self.user)
        token = utils.jwt_encode_handler(payload)
        response = self.client.get('/api/v1/plans/', HTTP_AUTHORIZATION="jwt " + str(token))
        self.assertEqual(response.status_code, 200)

    def test_get_plan_detail(self):
        """
            Get detail of a master admin user
        """
        payload = utils.jwt_payload_handler(self.user)
        token = utils.jwt_encode_handler(payload)
        response = self.client.get('/api/v1/plans/' + str(self.plan.id) + '/',
                                   HTTP_AUTHORIZATION="jwt " + str(token))
        self.assertEqual(response.status_code, 200)

    def test_delete_plan(self):
        """
            Delete the master admin
        """
        payload = utils.jwt_payload_handler(self.user)
        token = utils.jwt_encode_handler(payload)
        response = self.client.delete('/api/v1/plans/' + str(self.plan.id) + '/',
                                      HTTP_AUTHORIZATION="jwt " + str(token))
        self.assertEqual(response.status_code, 204)

    def test_update_plan(self):
        """
            update the master admin
            name = models.CharField(max_length=50)      #Name of the plan
            creation_time = models.DateTimeField(auto_now=True)
            deletion_time = models.DateTimeField(auto_now=False, null=True, default=None)
            deleted = models.BooleanField(default=False)

        """
        payload = utils.jwt_payload_handler(self.user)
        token = utils.jwt_encode_handler(payload)
        response = self.client.put('/api/v1/plans/' + str(self.plan.id) + '/',
                                   data={"name": "Demo now", "creation_time": "2016-04-07 16:09:54.462705+05:30", "deletion_time": "2016-04-07 16:09:54.462705+05:30", "deleted": False }, HTTP_AUTHORIZATION="jwt " + str(token))
        self.assertEqual(response.status_code, 200)

    def test_partial_plan(self):
        """
            partial update the master admin
        """
        payload = utils.jwt_payload_handler(self.user)
        token = utils.jwt_encode_handler(payload)
        response = self.client.patch('/api/v1/plans/' + str(self.plan.id) + '/',
                                     data={"name": "Demo new"}, HTTP_AUTHORIZATION="jwt " + str(token))
        self.assertEqual(response.status_code, 200)


class PlanViewTestCase(APITestCase):
    """
        This is the test case to check the TrackingDataView API is working well or not
    """

    def setUp(self):
        """

        """
        pass

    def test_tracking_data(self):
        """

        """
        pass

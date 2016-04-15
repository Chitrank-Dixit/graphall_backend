from django.contrib.auth.models import User
from administration.models import Plan
from django.test import TestCase
from authentication.models import MasterAdmin, Client


class MasterAdminTestCase(TestCase):
    def setUp(self):
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

    def master_admin_username(self):
        master_admin_username = MasterAdmin.objects.get(pk=self.masteradmin.pk).__unicode__()
        self.assertEqual(master_admin_username, self.masteradmin.user.username)


class ClientTestCase(TestCase):
    def setUp(self):
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

    def client_username(self):
        client_username = Client.objects.get(pk=self.client.pk).__unicode__()
        self.assertEqual(client_username, self.clients.user.username)
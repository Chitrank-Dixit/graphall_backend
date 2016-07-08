from django.contrib.auth.models import User
from django.test import TestCase
from administration.models import Plan
from ..models import Tag, TrackingSource
from authentication.models import Client


__author__ = 'chitrankdixit'


class TagTestCase(TestCase):
    def setUp(self):
        self.tagname = "Demo 1"
        self.tag = Tag.objects.create(name=self.tagname)


    def get_tag_name(self):
        tag_name = Tag.objects.get(pk=self.tag.pk).__unicode__()
        self.assertEqual(tag_name, self.tagname)


class TrackingSourceCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="chitrankdixit"
        )
        self.plan = Plan.objects.create(
            name="Demo"
        )
        self.client = Client.objects.create(
            plan_id = self.plan.id,
            user_id = self.user.id
        )
        self.tracking_source_name = "Dogs Home"
        self.tracking_source = TrackingSource.objects.create(
            name = self.tracking_source_name,
            website = "http://dogshome.com",
            industry_category = '2',
            client_id = self.client.id
        )

    def get_tracking_source_name(self):
        tracking_source_name = TrackingSource.objects.get(pk=self.tracking_source.pk).__unicode__()
        #import pdb;pdb.set_trace()
        self.assertEqual(str(tracking_source_name), self.tracking_source_name)





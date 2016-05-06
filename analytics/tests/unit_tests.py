from django.test import TestCase
from analytics.models import Tag

__author__ = 'chitrankdixit'


class TagTestCase(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Demo 1")


    def get_plan_name(self):
        tag_name = Tag.objects.get(pk=self.tag.pk).__unicode__()
        self.assertEqual(tag_name, 'Demo 1')

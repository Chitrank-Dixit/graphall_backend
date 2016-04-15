__author__ = 'chitrankdixit'

from django.test import TestCase
from administration.models import Plan

class PlanTestCase(TestCase):
    def setUp(self):
        self.plan = Plan.objects.create(name="Demo 1")


    def get_plan_name(self):
        plan_name = Plan.objects.get(pk=self.plan.pk).__unicode__()
        self.assertEqual(plan_name, 'Demo 1')


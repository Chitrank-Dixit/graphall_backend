from django.db import models
from utils import ChoiceEnum
# Create your models here.

class IndustryCategory(ChoiceEnum):
    Education = 1
    Medical = 2
    Sports = 3
    Entertainment = 4
    Government = 5
    Personal = 6
    Ecommerce = 7
    Realestate = 8


class TrackingSource(models.Model):
    tracking_id = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    website = models.CharField(max_length=200)
    industry_category = models.CharField(max_length=1,choices=IndustryCategory.choices(),default='1')
    creation_time = models.DateTimeField(auto_now=True)
    deletion_time = models.DateTimeField(auto_now=False, null=True, default=None)
    is_active = models.BooleanField(default=True)



class TrackingSourceDetails(models.Model):
    tracking_source = models.ForeignKey(TrackingSource)
    page_url = models.CharField(max_length=200)
    page_views = models.IntegerField()
    page_clicks = models.IntegerField()
    creation_time = models.DateTimeField(auto_now=True)
    deletion_time = models.DateTimeField(auto_now=False, null=True, default=None)
    is_active = models.BooleanField(default=True)



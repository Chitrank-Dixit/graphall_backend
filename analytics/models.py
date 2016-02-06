import random
from django.db import models
from utils import ChoiceEnum
from datetime import datetime
from django.contrib.auth.models import User
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

class WebBrowser(ChoiceEnum):
    chrome = 1
    firefox = 2
    safari = 3
    ie = 4
    opera = 5


class Day(ChoiceEnum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday = 7


class Month(ChoiceEnum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June =6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.name



class TrackingSource(models.Model):
    tracking_id = models.CharField(max_length=20,unique=True, default='GPAL-'+''.join([str(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')) for i in xrange(6)]))
    name = models.CharField(max_length=50)
    website = models.CharField(max_length=200)
    industry_category = models.CharField(max_length=1,choices=IndustryCategory.choices(),default='1')
    creation_time = models.DateTimeField(auto_now=True)
    deletion_time = models.DateTimeField(auto_now=False, null=True, default=None)
    tag = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, null=True)
    is_active = models.BooleanField(default=True)

    def get_tag_details(self):
        return " , ".join([p.name for p in self.tag.all()])



    def __unicode__(self):
        return self.name


class TrackingSourceDetails(models.Model):
    tracking_source = models.ForeignKey(TrackingSource)
    page_url = models.CharField(max_length=200, unique=True)
    page_views = models.IntegerField()
    page_clicks = models.IntegerField()
    web_browser = models.CharField(max_length=1,choices=WebBrowser.choices(), default='1')
    creation_time = models.DateTimeField(auto_now=True)
    deletion_time = models.DateTimeField(auto_now=False, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def get_tracking_source_name(self):
        if (self.tracking_source.name):
            return "%s"%(self.tracking_source.name)
        else:
            return "Not Applicable"

    def get_tracking_source_tracking_id(self):
        if (self.tracking_source.tracking_id):
            return "%s"%(self.tracking_source.tracking_id)
        else:
            return "Not Applicable"

    def __unicode__(self):
        return self.page_url

    class Meta:
        abstract = True




class TrackingSourceDetailsLog(TrackingSourceDetails):
    a = models.CharField(max_length=1, default='1')



class TrackingSourceDetailsDaily(TrackingSourceDetails):
    day = models.CharField(max_length=1,choices=Day.choices(), default='1')



class TrackingSourceDetailsWeekly(TrackingSourceDetails):
    a = models.CharField(max_length=1, default='1')



class TrackingSourceDetailsMonthly(TrackingSourceDetails):
    month = models.CharField(max_length=1,choices=Month.choices(), default='1')


class TrackingSourceDetailsYearly(TrackingSourceDetails):
    a = models.CharField(max_length=1, default='1')
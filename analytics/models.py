import random
from django.db import models
from authentication.models import Client, MasterAdmin
from miscellaneous.models import TimeStampMixin
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


class Tag(TimeStampMixin):
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.name


class TrackingSource(TimeStampMixin):
    tracking_id = models.CharField(max_length=20,unique=True, default='GPAL-'+''.join([str(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')) for i in xrange(6)]))
    name = models.CharField(max_length=50)
    website = models.CharField(max_length=200)
    industry_category = models.CharField(max_length=1,choices=IndustryCategory.choices(),default='1')
    creation_time = models.DateTimeField(auto_now=True)
    deletion_time = models.DateTimeField(auto_now=False, null=True, default=None)
    tag = models.ManyToManyField(Tag)
    client = models.ForeignKey(Client, null=True)
    master_admin = models.ForeignKey(MasterAdmin, null=True)
    is_active = models.BooleanField(default=True)

    def get_tag_details(self):
        return " , ".join([p.name for p in self.tag.all()])

    def __unicode__(self):
        return self.name


class TrackingSourceDetails(TimeStampMixin):
    tracking_source = models.ForeignKey(TrackingSource)
    page_url = models.CharField(max_length=200, default=' ')
    page_views = models.IntegerField(default=0)
    page_clicks = models.IntegerField(default=0)
    web_browser = models.CharField(max_length=1,choices=WebBrowser.choices(), default='1')
    event_date = models.DateField(auto_now=True , null=True)
    creation_time = models.DateTimeField(auto_now=True)
    deletion_time = models.DateTimeField(auto_now=False, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def get_tracking_source_name(self):
        if self.tracking_source.name:
            return "%s" % self.tracking_source.name
        else:
            return "Not Applicable"

    def get_tracking_source_tracking_id(self):
        if self.tracking_source.tracking_id:
            return "%s" % self.tracking_source.tracking_id
        else:
            return "Not Applicable"

    def __unicode__(self):
        return self.page_url

    class Meta:
        abstract = True


class TrackingSourceDetailsLog(TrackingSourceDetails):
    a = models.CharField(max_length=1, default='1')


# database view django: https://docs.djangoproject.com/en/1.8/ref/models/options/#django.db.models.Options.managed
# more on this: https://code.djangoproject.com/ticket/3361 (old)
# also can be used the modules: https://pypi.python.org/pypi/django-database-view/0.1.2

# class TrackingSourceDetailsFilter(TrackingSourceDetails):
#     day = models.CharField(max_length=1, choices=Day.choices(), null=True, default='1')
#
#     class Meta:
#         managed = False


# class TrackingSourceDetailsDaily(models.Views):
#     tracking_source = TrackingSourceDetails.tracking_source
#     page_url = TrackingSourceDetails.page_url
#     page_views  = TrackingSourceDetails.page_views
#     page_clicks = TrackingSourceDetails.page_clicks
#     web_browser = TrackingSourceDetails.web_browser
#     event_date = TrackingSourceDetails.event_date
#     is_active = TrackingSourceDetails.is_active


# class TrackingSourceDetailsLog(TrackingSourceDetails):
#     a = models.CharField(max_length=1, default='1')


# class TrackingSourceDetailsDaily(TrackingSourceDetails):
#     day = models.CharField(max_length=1, choices=Day.choices(), null=True, default='1')
#
#
# class TrackingSourceDetailsWeekly(TrackingSourceDetails):
#     a = models.CharField(max_length=1, default='1')
#
#
# class TrackingSourceDetailsMonthly(TrackingSourceDetails):
#     month = models.CharField(max_length=1,choices=Month.choices(), default='1')
#
#
# class TrackingSourceDetailsYearly(TrackingSourceDetails):
#     a = models.CharField(max_length=1, default='1')
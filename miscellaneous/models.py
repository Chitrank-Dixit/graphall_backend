from datetime import datetime
from django.contrib.gis.db.models import PointField
from django.db import models

# Create your models here.
from django.utils import timezone


class TimeStampMixin(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     """ On save, update timestamps """
    #     if not self.id:
    #         self.created_on = timezone.now()
    #     self.updated_on = timezone.now()
    #
    #     return super(TimeStampMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class AddressMixin(models.Model):
    """
        To Store the place_id by google API
    """
    place_id = models.CharField(max_length=100, blank=True)
    geo_coordinates = PointField(null=True, blank=True,)
    pin_code = models.CharField(max_length=20, blank=True)  # TODO: clean the data and reduce the max_length
    address = models.TextField(max_length=200, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    class Meta:
        abstract = True

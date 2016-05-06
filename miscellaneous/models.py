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
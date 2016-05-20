from django.db import models
from miscellaneous.models import TimeStampMixin


class Plan(TimeStampMixin):
    """
        Usage plan to use
    """

    name = models.CharField(max_length=50, unique=True)      # name of the plan should always be unique
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name
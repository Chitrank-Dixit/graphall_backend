from django.db import models

class Plan(models.Model):
    """
        Usage plan to use
    """

    name = models.CharField(max_length=50, unique=True)      # name of the plan should always be unique
    creation_time = models.DateTimeField(auto_now=True)
    deletion_time = models.DateTimeField(auto_now=False, null=True, default=None)
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name
from django.db import models
from django.contrib.auth.models import User
from administration.models import Plan


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    registered_type = models.IntegerField(default=0)

    class Meta:
        abstract = True


class Client(UserProfile):
	plan = models.ForeignKey(Plan, related_name="Planwise_Clients")
	

    




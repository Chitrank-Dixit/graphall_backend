from django.db import models
from django.contrib.auth.models import User
from administration.models import Plan


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    registered_type = models.IntegerField(default=0)
    address = models.CharField(max_length=100, null=True)
    mobile_phone = models.IntegerField(default=0)

    class Meta:
        abstract = True


class Client(UserProfile):
    plan = models.ForeignKey(Plan, related_name="planwise_clients")
    user_type = models.IntegerField(default=1)



class MasterAdmin(UserProfile):
    user_type = models.IntegerField(default=2)





from django.db import models
from django.contrib.auth.models import User
from administration.models import Plan
from django.core.validators import RegexValidator


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    registered_type = models.IntegerField(default=0)
    address = models.CharField(max_length=100, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=15)

    class Meta:
        abstract = True


class Client(UserProfile):
    plan = models.ForeignKey(Plan, related_name="planwise_clients", null=True)
    user_type = models.IntegerField(default=1)



class MasterAdmin(UserProfile):
    user_type = models.IntegerField(default=2)





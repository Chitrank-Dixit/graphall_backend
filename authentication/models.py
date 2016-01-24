from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from administration.models import Plan
from utils import ChoiceEnum


class UserType(ChoiceEnum):
    client = 1
    masteradmin = 2

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    registered_type = models.IntegerField(default=0)
    address = models.CharField(max_length=100, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=15)

    def get_user_name(self):
        if(self.user.username):
            return "%s"%(self.user.username)
        else:
            return "None"

    def __unicode__(self):
        return self.user.username

    class Meta:
        abstract = True


class Client(UserProfile):
    plan = models.ForeignKey(Plan, related_name="planwise_clients", null=True)
    user_type = models.CharField(max_length=1,choices=UserType.choices(),default='1')



class MasterAdmin(UserProfile):
    user_type = models.CharField(max_length=1,choices=UserType.choices(),default='2')





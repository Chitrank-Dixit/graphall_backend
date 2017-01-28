from datetime import timedelta
from time import timezone
from oauth2_provider.models import AccessToken, Application

__author__ = 'chitrankdixit'
import inspect
from enum import Enum

class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        # get all members of the class
        members = inspect.getmembers(cls, lambda m: not(inspect.isroutine(m)))
        # filter down to just properties
        props = [m for m in members if not(m[0][:2] == '__')]
        # format into django choice tuple
        choices = tuple([(str(p[1]), p[0]) for p in props])
        return choices

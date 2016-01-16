import re
from django.http import HttpRequest, HttpResponse

__author__ = 'chitrankdixit'
import inspect
from enum import Enum

whitedomain_list = ["http://localhost:9000","http://localhost:8000","http://web-staging.flyrobeapp.com","https://web-staging.flyrobeapp.com","http://localhost:63342","http://localhost:63343","http://central.flyrobeapp.com","http://flyrobe.com","https://flyrobe.com","http://web-central.flyrobeapp.com","http://app-central.flyrobeapp.com"]
whitehost_list = ["central.flyrobeapp.com","staging.flyrobeapp.com","web-staging.flyrobeapp.com","web-central.flyrobeapp.com","app-central.flyrobeapp.com","flyrobe.com","localhost:8000","127.0.0.1:8000","web-central.flyrobeapp.com","app-central.flyrobeapp.com"]

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

def set_response_header(**kwargs):
    #pdb.set_trace()
    pattern=re.compile("^chrome-extension://*")
    if isinstance(kwargs['request'],HttpRequest) and isinstance(kwargs['response'],HttpResponse):
        if kwargs['request'].META.has_key('HTTP_ORIGIN') and kwargs['request'].META['HTTP_ORIGIN'] in whitedomain_list:
            kwargs['response']['Access-Control-Allow-Credentials']='true'
            kwargs['response']['Access-Control-Allow-Methods']="GET, POST, OPTIONS, DELETE, PUT"
            kwargs['response']['Access-Control-Allow-Origin']="*"
            #kwargs['response']['Access-Control-Allow-Origin']="http://web-staging.flyrobeapp.com/, http://localhost:8000/"
            kwargs['response']['Access-Control-Max-Age']="1728000"
            kwargs['response']['Cache-Control']="max-age=0, private, must-revalidate"
            kwargs['response'].__delitem__("X-Frame-Options")
            return True,kwargs['response']
        elif kwargs['request'].META.has_key('HTTP_ORIGIN') and pattern.match(kwargs['request'].META['HTTP_ORIGIN']):
            return True,kwargs['response']
        elif kwargs['request'].META.has_key('HTTP_HOST') and kwargs['request'].META['HTTP_HOST'] in whitehost_list:
            kwargs['response']['Access-Control-Allow-Credentials']='true'
            kwargs['response']['Access-Control-Allow-Methods']="GET, POST, OPTIONS, DELETE, PUT"
            kwargs['response']['Access-Control-Allow-Origin']="*"
            #kwargs['response']['Access-Control-Allow-Origin']="http://web-staging.flyrobeapp.com/, http://localhost:8000/"
            kwargs['response']['Access-Control-Max-Age']="1728000"
            kwargs['response']['Cache-Control']="max-age=0, private, must-revalidate"
            kwargs['response'].__delitem__("X-Frame-Options")
            return True,kwargs['response']
        elif not kwargs['request'].META.has_key('HTTP_ORIGIN') and not kwargs['request'].META.has_key('HTTP_HOST'):
            return True,kwargs['response']
    else:
        return False,kwargs['response']

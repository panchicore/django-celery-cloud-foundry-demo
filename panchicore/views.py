from django.http import HttpResponse
from tasks import add
import requests

def home(request):
    test = add.delay(1, 1)
    print test.__dict__
    return HttpResponse("OK=" +  str(test.__dict__))
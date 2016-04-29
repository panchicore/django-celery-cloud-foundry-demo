import os
import json
import requests
import time
from celery import Celery


BROKER_URL = 'redis://localhost:6379/0'

vcap_services =  os.getenv('VCAP_SERVICES', None)
if vcap_services:
    vcap_services = json.loads(vcap_services)
    rediscloud = vcap_services.get("rediscloud")[0]
    redis_url = 'redis://:{0}@{1}:{2}/0'.format(
        rediscloud["credentials"]["password"],
        rediscloud["credentials"]["hostname"],
        rediscloud["credentials"]["port"]
    )
    BROKER_URL = redis_url


app = Celery('tasks', broker=BROKER_URL)

@app.task
def add(x, y):
    print "SLEEPING..."
    time.sleep(30)
    print "DONE..."
    requests.get("http://requestb.in/pfnpmdpf")
    return x + y
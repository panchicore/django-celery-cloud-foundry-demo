# django-celery-cloud-foundry-demo


Deploy web and worker instance.
```
cf push -f manifest.yml
```

## disclaimer:

Could foundry health-checks requires service running on port $PORT so in worker manifest command run a local django server.
```
command: python manage.py runserver --insecure 0.0.0.0:$PORT & celery -A tasks worker --loglevel=info --concurrency=1
```


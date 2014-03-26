
from dzapgo import celery_app

import requests
import json

@celery_app.task()
def deliver_hook(target, payload, instance=None, hook=None, **kwargs):
    """
    target:     the url to receive the payload.
    payload:    a python primitive data structure
    instance:   a possibly null "trigger" instance
    hook:       the defining Hook object
    """
    requests.post(
        url=target,
        data=json.dumps(payload),
        headers={'Content-Type': 'application/json'}
    )

deliver_hook_wrapper = deliver_hook.delay
web: gunicorn --pythonpath dzapgo dzapgo.wsgi
worker: cd dzapgo && celery -A dzapgo worker -l info

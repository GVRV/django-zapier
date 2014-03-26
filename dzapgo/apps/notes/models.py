
from datetime import datetime

from django.db import models
from rest_hooks.models import Hook


class Note(models.Model):
    title = models.CharField(max_length=140)
    updated_at = models.DateTimeField(default=datetime.now())
    content = models.TextField()

    def __unicode__(self):
        return self.title 

    def save(self, **kwargs):
        return super(Note, self).save()


# Monkey patching Hooks to always be associated 
# with User pk=1 cause we want it to be free-for-all
# This is bad, mkayyy
Hook._meta.fields[3].default = 1

from datetime import datetime

from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=140)
    updated_at = models.DateTimeField(default=datetime.now())
    content = models.TextField()

    def __unicode__(self):
        return self.title 

    def save(self, **kwargs):
        return super(Note, self).save()
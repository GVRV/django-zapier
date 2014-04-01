
from django.shortcuts import render

from rest_hooks.signals import hook_event

from .models import Note


def homepage(request):
    note = Note.objects.first()
    hook_event.send(
            sender=note.__class__,
            action='note.viewed',
            instance=note
        )
    return render(request, 'homepage.html', {
        'note': note
        })

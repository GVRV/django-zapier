
from django.shortcuts import render

from .models import Note


def homepage(request):
    note = Note.objects.first() 
    return render(request, 'homepage.html', {
        'note': note
        })
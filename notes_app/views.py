from django.shortcuts import render
from .models import Note

# Create your views here.

def notes_list (req) :
    notes = Note.objects.all()
    return render(req , "notes_app/notes_list.html" , {"notes" : notes})

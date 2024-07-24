from django.shortcuts import render
from django.utils.translation import activate


# Create your views here.

def home(request, lang='es'):
    activate(lang)
    return render(request, 'home.html')

def scheduled(request, lang='es'):
    activate(lang)
    return render(request, 'scheduled.html')
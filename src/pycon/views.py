from django.shortcuts import render
from django.utils.translation import activate


# Create your views here.

def home(request, lang='es'):
    activate(lang)
    return render(request, 'home.html')

def conduct(request, lang='es'):
    activate(lang)
    return render(request, 'conduct.html')
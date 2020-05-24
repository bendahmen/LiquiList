from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def home(request):
    """ Calendar Weeks payment overview """
    receivables = Receivable.objects.all()
    return render(request, 'cwView.html', {'receivables': receivables})

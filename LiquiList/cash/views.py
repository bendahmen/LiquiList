from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def home(request):
    """ Calendar Weeks payments overview """
    cWeeks = {1: dict(), 2: dict(), 3: dict(), 4: dict()}
    for week in range(1, 5):
        cWeeks[week]['receivables'] = Receivable.objects.all()
        cWeeks[week]['payables'] = Payable.objects.all()
    return render(request, 'cwView.html', {'cWeeks': cWeeks})

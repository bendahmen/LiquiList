from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *

def home(request):
    """ Calendar Weeks payments overview """


    #Post request
    if request.method == 'POST':
        paymentID = request.POST['paymentID']
        cw = request.POST['cwxxSelector']
        paymentType = request.POST['paymentTypeForm']

        if paymentType == 'receivables':
            currentPayment = Receivable.objects.get(pk = paymentID)
            currentPayment.week = cw
            currentPayment.save()
        else:
            currentPayment = Payable.objects.get(pk = paymentID)
            currentPayment.week = cw
            currentPayment.save()

        return redirect('home')



    accounts = Account.objects.all()

    cWeeks = {1: dict(), 2: dict(), 3: dict(), 4: dict()}
    for week in range(1, 5):
        cWeeks[week]['receivables'] = Receivable.objects.filter(week=week)
        cWeeks[week]['payables'] = Payable.objects.filter(week=week)
    return render(request, 'cwView.html', {'cWeeks': cWeeks, 'accounts': accounts})

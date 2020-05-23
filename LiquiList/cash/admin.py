from django.contrib import admin
from .models import Payable, Receivable, Recurrent, Account, PlanStatus, TypeStatus

# Register your models here.
admin.site.register(Payable)
admin.site.register(Receivable)
admin.site.register(Recurrent)
admin.site.register(Account)
admin.site.register(PlanStatus)
admin.site.register(TypeStatus)

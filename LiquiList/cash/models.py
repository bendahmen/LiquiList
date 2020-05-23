from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=60)
    balance = models.IntegerField()
    updateCW = models.IntegerField()

    def __str__(self):
        return self.name

class Receivable(models.Model):
    amount = models.IntegerField()
    customer = models.CharField(max_length=60)
    week = models.IntegerField()
    account = models.ForeignKey(Account, related_name='receivables', on_delete=models.CASCADE)

class Recurrent(models.Model):
    amount = models.IntegerField()
    customer = models.CharField(max_length=60)
    frequency = models.IntegerField()
    account = models.ForeignKey(Account, related_name='recurrents', on_delete=models.CASCADE)

class PlanStatus(models.Model):
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.status

class TypeStatus(models.Model):
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.status

class Payable(models.Model):
    """ payment item """
    amount = models.IntegerField()
    customer = models.CharField(max_length=60)
    week = models.IntegerField()
    planStatus = models.ForeignKey(PlanStatus, related_name='payables', on_delete=models.CASCADE)
    typeStatus = models.ForeignKey(TypeStatus, related_name='payables', on_delete=models.CASCADE)
    account = models.ForeignKey(Account, related_name='payables', on_delete=models.CASCADE)

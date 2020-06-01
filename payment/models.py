from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Payment(models.Model):
    patient_name = models.CharField(max_length=30)
    Total_amount = models.IntegerField()
    Deposit = models.IntegerField()

    Insurance = models.IntegerField()
    collection_date = models.CharField(max_length=10)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.patient_name

    def get_absolute_url(self):
        return reverse('payment_details', kwargs={'pk': self.pk})

    @property
    def balance_amount(self):
        if self.Total_amount > 1 and self.Deposit > 1:
            self.Balance = self.Total_amount - self.Deposit
            return self.Balance
        if self.Deposit == 0:
            self.Balance = 0
            return self.Balance
    
    @property
    def income(self):
        if self.Deposit == 0 and self.Total_amount > 1:
            self.total_income = self.Total_amount
            return self.total_income
        if self.Deposit > 1 and self.Total_amount > 1:
            self.total_income = self.Deposit
            return self.total_income   
        
         
from django.db import models
from accounts.models import Accounts

class Drug(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    acc_id = models.ForeignKey(Accounts, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.name

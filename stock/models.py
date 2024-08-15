from django.db import models
from drug.models import Drug

class Stock(models.Model):
    batch_id = models.CharField(max_length=5)
    drug_id = models.ForeignKey(Drug, on_delete=models.CASCADE)
    quantity = models.IntegerField()
 
    def __str__(self):
        return f"{self.drug_id.name} - {self.quantity}"

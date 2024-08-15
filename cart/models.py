from django.db import models
from accounts.models import Accounts
from drug.models import Drug

class Cart(models.Model):
    acc_id = models.ForeignKey(Accounts, on_delete=models.CASCADE)
 
    def __str__(self):
        return f"Cart {self.id} for {self.acc_id.org_name}"
 
class CartItem(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    drug_id = models.ForeignKey(Drug, on_delete=models.CASCADE)
    quantity = models.IntegerField()
 
    def __str__(self):
        return f"Cart {self.cart_id.acc_id.org_name}: {self.drug_id.name} - {self.quantity}"
from django.db import models
from django.contrib.auth.models import User


class OrderDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ctclid = models.CharField(max_length=100)
    contractName = models.CharField(max_length=100)
    assetName = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=4)
    quantity = models.PositiveIntegerField()
    side = models.CharField(max_length=10)
    lotside = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.contractName} - {self.assetName}"

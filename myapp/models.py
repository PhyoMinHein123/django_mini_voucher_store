from django.db import models

# Create your models here.
class Branch(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000, default=None)

    def __str__(self):
        return self.name

class Voucher(models.Model):
    id = models.AutoField(primary_key=True)
    counter_id = models.IntegerField(default=None)
    cashier_name = models.CharField(max_length=1000, default=None)
    customer_name = models.CharField(max_length=1000, default=None)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    date = models.DateField(default=None)
    total = models.IntegerField(default=None)
    items = models.JSONField(default=None, blank=True, null=True)
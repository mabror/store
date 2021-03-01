from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    amount = models.BigIntegerField()

    def __str__(self):
        return self.name

class Income(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    added = models.DateTimeField(auto_now_add=True)



class Outgoung(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    added = models.DateTimeField(auto_now_add=True)

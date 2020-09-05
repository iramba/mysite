from django.db import models


class Customer(models.Model):
    id = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.id


class Item(models.Model):
    name = models.CharField(max_length = 30)
    price = models.FloatField()

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

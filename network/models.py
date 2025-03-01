from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name


class NetworkNode(models.Model):
    LEVEL_CHOICES = [
        (0, "Factory"),
        (1, "Retail Network"),
        (2, "Individual Entrepreneur"),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)
    products = models.JSONField()
    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, null=True, blank=True
    )
    debt_to_supplier = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )
    created_at = models.DateTimeField(auto_now_add=True)
    level = models.IntegerField(choices=LEVEL_CHOICES)

    def __str__(self):
        return self.name

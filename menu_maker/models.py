from django.db import models

class Item(models.Model):
    product = models.CharField("Product", max_length=120)
    net_wt = models.CharField("Net Weight", max_length=120)
    rate = models.CharField("Rate", max_length=120)
    availability = models.CharField(
        "Availibility", 
        choices=[("yes", "Yes"),
                 ("no", "No")],
        max_length=120
        )

    def __str__(self):
        return self.product
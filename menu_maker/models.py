from django.db import models

class Item(models.Model):
    product = models.CharField("Product", max_length=120)
    cut_details = models.CharField("Cut Details", max_length=120)
    count = models.CharField("Count Per Kg", max_length=120)
    rate = models.CharField("Rate", max_length=120)
    availability = models.CharField(
        "Availibility", 
        choices=[("yes", "Yes"),
                 ("no", "No")],
        max_length=120
        )

    def __str__(self):
        return self.product
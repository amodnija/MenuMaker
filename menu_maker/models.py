from django.db import models

class Menu(models.Model):
    product = models.CharField("Product")
    weight = models.CharField("Weight")
    cut_details = models.CharFiels("Cut Details")
    count = models.CharField("Count Per Kg")
    rate = models.CharField("Rate")
    availability = models.CharField(
        "Availibility", 
        choices=[("yes", "Yes"),
                 ("no", "No")],
                                    
        )

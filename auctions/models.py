from django.db import models
from django.contrib.auth.models import User


class Auctions(models.Model):
    """
    Field model for categories of product.
    """
    productgategory_choices = [
        ('home', 'Home'),
        ('office', 'Office'),
        ('building', 'Building'),
        ('vehicle', 'Vehicle'),
        ('industry', 'Industry'),
        ('agriculture', 'Agriculture'),
    ]

    bidder_choices = [
        ('furniture', 'Furniture'),
        ('chair', 'Chair'),
        ('table', 'Table'),
        ('bicycle', 'Bicycle'),
        ('bed', 'Bed'),
        ('refrigerator', 'Refrigerator'),
        ('pc', 'Pc'),
        ('phones', 'Phones'),
    ]

    autocategory_choices = [
        ('car', 'Car'),
        ('minibus', 'Minibus'),
        ('truck', 'Truck'),
        ('bus', 'Bus'),
        ('escavator', 'Escavator'),
        ('motocycle', 'Motocycle'),
    ]

    fueltype_choices = [
        ('petrol', 'Petrol'),
        ('hybrid', 'Hybrid'),
        ('diesel', 'Diesel'),
        ('electric', 'Electric'),
    ]

    openingday_choices = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
    ]

   
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auction')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=20)
    productcategory = models.CharField(
        max_length=30, choices=productgategory_choices)
    bidder = models.CharField(max_length=30, choices=bidder_choices)
    autocategory = models.CharField(max_length=30, choices=autocategory_choices)
    openingday = models.CharField(
        max_length=30, choices=openingday_choices, default='monday')
    description = models.TextField()
    year = models.PositiveIntegerField()
    price = models.FloatField()
    image = models.ImageField(
        upload_to='images/', default='../default_post_dwzcuabfl'
    )
    fueltype = models.CharField(
        max_length=32, choices=fueltype_choices, default="petrol"
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.id} {self.title}"

from django.db import models
from django.contrib.auth.models import User


categories_choices = [
    ('home', 'Home'),
    ('office', 'Office'),
    ('building', 'Building'),
    ('vehicle', 'Vehicle'),
    ('industry', 'Industry'),
    ('agriculture', 'Agriculture'),
]

items_choices = [
    ('furniture', 'Furniture'),
    ('chair', 'Chair'),
    ('table', 'Table'),
    ('bicycle', 'Bicycle'),
    ('bed', 'Bed'),
    ('refrigerator', 'Refrigerator'),
    ('pc', 'Pc'),
    ('phones', 'Phones'),
    ('other', 'Other'),
]

auto_choices = [
    ('car', 'Car'),
    ('minibus', 'Minibus'),
    ('truck', 'Truck'),
    ('bus', 'Bus'),
    ('escavator', 'Escavator'),
    ('motocycle', 'Motocycle'),
    ('other', 'Other'),
]

fueltype_choices = [
    ('petrol', 'Petrol'),
    ('hybrid', 'Hybrid'),
    ('diesel', 'Diesel'),
    ('electric', 'Electric'),
    ('other', 'Other'),
]

auctionday_choices = [
    ('monday', 'Monday'),
    ('tuesday', 'Tuesday'),
    ('wednesday', 'Wednesday'),
    ('thursday', 'Thursday'),
]

class Auctions(models.Model):
    """
    Field model for categories of product.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auction')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=20)
    categories = models.CharField(
        max_length=30, choices=categories_choices)
    items = models.CharField(
        max_length=30, choices=items_choices, default='0')
    auto = models.CharField(
        max_length=30, choices=auto_choices, default='0')
    auctionday = models.CharField(
        max_length=30, choices=auctionday_choices, default='monday')
    description = models.TextField()
    year = models.PositiveIntegerField()
    price = models.FloatField()
    image = models.ImageField(
        blank=True, upload_to ="_images/", default="auction_image_dwzcuabfl"
    )
    fueltype = models.CharField(
        max_length=32, choices=fueltype_choices, default="petrol"
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.id} {self.title}"

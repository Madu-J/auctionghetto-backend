from django.db import models
from django.contrib.auth.models import User


class Auctions(models.Model):
    """
    Field model for categories of product.
    """
    auctions_choices = [
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
        ('motocycle', 'Motocycle'),
        ('pc', 'Pc'),
        ('car', 'Car'),
        ('phones', 'Phones'),
    ]

    openingday_choices = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
    ]

   
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=20)
    auctions = models.CharField(
        max_length=20, choices=auctions_choices)
    bidder = models.CharField(max_length=30, choices=bidder_choices)
    openingdays = models.CharField(
        max_length=30, choices=openingday_choices, default='monday')
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(
        upload_to='images/', default='../default_post_dwzcuabfl'
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.id} {self.title}"

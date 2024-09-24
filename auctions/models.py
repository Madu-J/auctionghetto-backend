from django.db import models
from django.contrib.auth.models import User


class Auction(models.Model):
    """
    This model provides field to create, retrieve or update
    postings in database by user instance.
    """

    categories_choices = [
        ('home', 'Home'),
        ('office', 'Office'),
        ('building', 'Building'),
        ('vehicle', 'Vehicle'),
        ('industry', 'Industry'),
        ('agriculture', 'Agriculture'),
        ('automobile', 'Automobile'),
        ('sports', 'Sports'),
        ('electronics', 'Electronics'),
    ]

    products_choices = [
        ('furniture', 'Furniture'),
        ('chair', 'Chair'),
        ('table', 'Table'),
        ('bicycle', 'Bicycle'),
        ('bed', 'Bed'),
        ('refrigerator', 'Refrigerator'),
        ('pc', 'Pc'),
        ('phones', 'Phones'),
        ('car', 'Car'),
        ('minibus', 'Minibus'),
        ('truck', 'Truck'),
        ('bus', 'Bus'),
        ('escavator', 'Escavator'),
        ('motocycle', 'Motocycle'),
        ('other', 'Other'),
    ]

    auctionday_choices = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=20)
    categories = models.CharField(
        max_length=30, choices=categories_choices, default='home'
    )
    products = models.CharField(
        max_length=30, choices=products_choices, default='phones')
    auctionday = models.CharField(
        max_length=30, choices=auctionday_choices, default='monday'
         )
    description = models.TextField()
    year = models.PositiveIntegerField()
    price = models.FloatField()
    image = models.ImageField(
        upload_to="images/", default="../default_auction_mvxwre"
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.id} {self.title}"

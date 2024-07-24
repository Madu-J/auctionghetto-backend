from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Auctioneer(models.Model):
    """
    Model for user profile (Auctioneer)
    """
    owner = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='auctioneer'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=12)
    postcode = models.CharField(max_length=6, null=True)
    street_address = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to="images/", default='../default_auctioneer_dwzcuabfl')

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.owner}'s auctioneer"

    def create_auctioneer(sender, instance, created, **kwargs):
        if created:
            Auctioneer.objects.create(owner=instance)

    post_save.connect(create_auctioneer, sender=User)

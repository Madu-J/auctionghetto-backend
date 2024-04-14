from django.db import models
from django.contrib.auth.models import User
from auctions.models import Auctions


class Bookmark(models.Model):
    """
    Bookmark model for auction items 'owner' is a User instance
    and 'auctions' is a Auctions instance. 'unique_together' prevent
    a user from bookmarking same item twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    auctions = models.ForeignKey(
        Auctions, on_delete=models.CASCADE, related_name="bookmark"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["owner", "auctions"]

    def __str__(self):
        return f"{self.owner} {self.auctions}"
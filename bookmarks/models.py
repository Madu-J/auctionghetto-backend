from django.db import models
from django.contrib.auth.models import User
from auctions.models import Auction


class Bookmark(models.Model):
    """
    Bookmark model for auction items 'owner' is a User instance
    and 'auction' is a Auctions instance. 'unique_together' prevent
    a user from bookmarking same item twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ForeignKey(
        Auction, on_delete=models.CASCADE,
        default=None, related_name="bookmarks")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["owner", "auction"]

    def __str__(self):
        return f"{self.owner} {self.auction}"

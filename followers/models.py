from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """Follower Model.
    Related to 'owner' and 'followed'user instances.
    'owner' is a User that is following a User and
    'followed' is a User that is followed by 'owner'.
    'unique_together' prevents duplicate followers.
    """

    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="following"
    )
    followed = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="followed"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["owner", "followed"]

    def __str__(self):
        return f"{self.owner} {self.followed}"

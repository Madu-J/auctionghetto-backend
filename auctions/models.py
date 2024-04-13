from django.db import models
from django.contrib.auth.models import User


class Auctions(models.Model):
    """
    Field model for categories of product.
    """
    auctions_choices = [
        ('home', 'Home', 'furniture'),
        ('office', 'Office', 'electronics'),
        ('building', 'Building'),
        ('vehicle', 'Vehicle'),
        ('industry', 'Industry'),
        ('agriculture', 'Agriculture'),
    ]
   
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=120)
    detail = models.TextField(null=True)

    price = models.FloatField()
    image = models.ImageField(
        upload_to='images/', default='../default_post_dwzcuabfl'
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.id} {self.title}"

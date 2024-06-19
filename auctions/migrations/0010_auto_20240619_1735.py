# Generated by Django 3.2.19 on 2024-06-19 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20240618_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctions',
            name='auctioneer_image',
        ),
        migrations.AddField(
            model_name='auctions',
            name='image',
            field=models.ImageField(blank=True, default='auction_image_dwzcuabfl', upload_to='_images/'),
        ),
    ]
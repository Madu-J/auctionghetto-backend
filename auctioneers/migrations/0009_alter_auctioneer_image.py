# Generated by Django 3.2.19 on 2024-09-24 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctioneers', '0008_alter_auctioneer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctioneer',
            name='image',
            field=models.ImageField(default='../auctioneer_image', upload_to='images/'),
        ),
    ]

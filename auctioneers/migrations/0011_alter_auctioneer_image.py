# Generated by Django 3.2.19 on 2024-09-29 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctioneers', '0010_alter_auctioneer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctioneer',
            name='image',
            field=models.ImageField(default='images/default_auctioneer_amxaod', upload_to='images/'),
        ),
    ]

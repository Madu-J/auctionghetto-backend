# Generated by Django 3.2.19 on 2024-06-28 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_auto_20240620_1656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctions',
            name='fueltype',
        ),
        migrations.AlterField(
            model_name='auctions',
            name='image',
            field=models.ImageField(default='post_image', upload_to='images/'),
        ),
    ]
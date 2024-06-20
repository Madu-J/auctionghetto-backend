# Generated by Django 3.2.19 on 2024-06-20 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctioneers', '0003_auto_20240618_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctioneer',
            name='auctioneer_image',
        ),
        migrations.AddField(
            model_name='auctioneer',
            name='image',
            field=models.ImageField(blank=True, default='default.webp', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='auctioneer',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='auctioneer',
            name='postcode',
            field=models.CharField(max_length=6, null=True),
        ),
    ]

# Generated by Django 3.2.19 on 2024-05-02 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20240502_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auctions',
            old_name='productcategory',
            new_name='categories',
        ),
    ]
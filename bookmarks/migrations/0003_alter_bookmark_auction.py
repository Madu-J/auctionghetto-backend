# Generated by Django 3.2.19 on 2024-07-09 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_alter_auction_categories'),
        ('bookmarks', '0002_auto_20240628_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='auction',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='bookmarks', to='auctions.auction'),
        ),
    ]

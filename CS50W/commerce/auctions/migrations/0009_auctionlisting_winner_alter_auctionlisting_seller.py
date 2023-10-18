# Generated by Django 4.2.4 on 2023-08-29 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0008_auctionlisting_is_closed"),
    ]

    operations = [
        migrations.AddField(
            model_name="auctionlisting",
            name="winner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="won_listings",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="auctionlisting",
            name="seller",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="seller_listings",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-28 20:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0003_alter_auctionlisting_current_bid"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="auctionlisting",
            name="end_time",
        ),
    ]
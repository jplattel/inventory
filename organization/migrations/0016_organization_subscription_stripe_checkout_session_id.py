# Generated by Django 2.2.9 on 2020-03-19 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("organization", "0015_auto_20200319_0944")]

    operations = [
        migrations.AddField(
            model_name="organization",
            name="subscription_stripe_checkout_session_id",
            field=models.CharField(default="", max_length=255),
        )
    ]

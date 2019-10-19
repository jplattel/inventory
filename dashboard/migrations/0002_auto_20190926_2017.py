# Generated by Django 2.2.5 on 2019-09-26 20:17

import django.db.models.deletion
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("dashboard", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="mutation",
            name="contra_mutation",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="dashboard.Mutation",
            ),
        ),
        migrations.AddField(
            model_name="mutation",
            name="operation",
            field=model_utils.fields.StatusField(
                choices=[(0, "dummy")],
                default="add",
                max_length=100,
                no_check_for_status=True,
            ),
        ),
        migrations.AlterField(
            model_name="inventory", name="amount", field=models.FloatField(default=0.0)
        ),
    ]

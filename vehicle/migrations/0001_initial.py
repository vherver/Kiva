# Generated by Django 5.0.1 on 2024-02-06 04:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("model", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Vehicle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, null=True),
                ),
                ("updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "deleted",
                    models.DateTimeField(blank=True, default=None, null=True),
                ),
                ("year", models.IntegerField()),
                ("serial", models.CharField(max_length=100)),
                (
                    "model",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="model.subbrand",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
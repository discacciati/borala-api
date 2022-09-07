# Generated by Django 4.1.1 on 2022-09-07 14:30

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="LineUp",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.UUID("39fc0d52-be68-487a-9ffe-8c8a41a7ac83"),
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("hour", models.TimeField()),
                ("description", models.TextField()),
                ("price", models.FloatField(default=0)),
                ("talent", models.TextField()),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lineup",
                        to="events.event",
                    ),
                ),
            ],
        ),
    ]
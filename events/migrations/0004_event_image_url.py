# Generated by Django 4.1.1 on 2022-09-12 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0003_alter_event_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="image_url",
            field=models.TextField(null=True),
        ),
    ]

# Generated by Django 5.0 on 2024-02-09 23:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bills", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="bills",
            name="is_approved",
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name="bills",
            name="status",
            field=models.CharField(blank=True, default="pending", max_length=20),
        ),
    ]
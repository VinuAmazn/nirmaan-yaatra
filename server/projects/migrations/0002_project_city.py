# Generated by Django 5.0 on 2024-02-02 16:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="city",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
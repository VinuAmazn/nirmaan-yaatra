# Generated by Django 5.0 on 2024-01-26 04:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "__first__"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="contractor",
            name="projects",
            field=models.ManyToManyField(blank=True, to="projects.project"),
        ),
    ]

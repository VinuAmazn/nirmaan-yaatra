# Generated by Django 5.0 on 2024-02-10 00:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tasks",
            name="end_date",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="tasks",
            name="start_date",
            field=models.DateField(),
        ),
    ]
# Generated by Django 4.2.17 on 2025-02-14 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("healthproapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="healthpro",
            name="certification",
            field=models.FileField(blank=True, null=True, upload_to="certifications/"),
        ),
        migrations.AlterField(
            model_name="healthpro",
            name="specialization",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

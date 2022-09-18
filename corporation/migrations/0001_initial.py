# Generated by Django 4.1.1 on 2022-09-18 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Corporation",
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
                ("name", models.CharField(blank=True, max_length=250, null=True)),
                ("address", models.CharField(blank=True, max_length=250, null=True)),
                ("phone", models.CharField(blank=True, max_length=250, null=True)),
                ("open_hours", models.CharField(blank=True, max_length=250, null=True)),
                ("link", models.URLField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
    ]

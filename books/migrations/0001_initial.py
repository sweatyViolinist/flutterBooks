# Generated by Django 5.0.4 on 2024-04-22 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                    "cover",
                    models.ImageField(blank=True, null=True, upload_to="covers/"),
                ),
                ("title", models.CharField(max_length=60)),
                ("author", models.CharField(max_length=60)),
                ("year", models.IntegerField()),
                ("content", models.TextField()),
            ],
        ),
    ]

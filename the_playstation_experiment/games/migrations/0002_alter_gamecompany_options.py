# Generated by Django 4.2.1 on 2023-05-17 01:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("games", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="gamecompany",
            options={"verbose_name_plural": "game companies"},
        ),
    ]
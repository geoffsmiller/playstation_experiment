# Generated by Django 4.2.1 on 2023-05-18 01:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("episodes", "0007_remove_segment_game"),
    ]

    operations = [
        migrations.RenameField(
            model_name="segment",
            old_name="title",
            new_name="title_override",
        ),
    ]
# Generated by Django 4.2.2 on 2023-07-16 22:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("episodes", "0015_alter_episode_series_alter_segment_episode_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="segment",
            name="segment_type",
            field=models.CharField(
                choices=[
                    ("Content Warning", "Content Warning"),
                    ("OP", "Opening"),
                    ("Intro", "Intro"),
                    ("Feature", "Feature"),
                    ("Review", "Review"),
                    ("Chapter", "Chapter"),
                    ("Release Roundup", "Release Roundup"),
                    ("Outro", "Outro"),
                ],
                max_length=128,
            ),
        ),
    ]

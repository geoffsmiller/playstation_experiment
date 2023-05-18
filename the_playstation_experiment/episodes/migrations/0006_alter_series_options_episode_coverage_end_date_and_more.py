# Generated by Django 4.2.1 on 2023-05-18 00:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("episodes", "0005_series_order"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="series",
            options={"ordering": ["order"], "verbose_name_plural": "series"},
        ),
        migrations.AddField(
            model_name="episode",
            name="coverage_end_date",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="episode",
            name="coverage_start_date",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="episode",
            name="release_date",
            field=models.DateField(null=True),
        ),
    ]

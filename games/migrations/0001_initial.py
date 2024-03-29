# Generated by Django 4.2.1 on 2023-05-16 23:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Game",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=1028)),
            ],
        ),
        migrations.CreateModel(
            name="GameCompany",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=1028)),
            ],
        ),
        migrations.CreateModel(
            name="GamePlatform",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=1028)),
            ],
        ),
        migrations.CreateModel(
            name="GameRelease",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=1028)),
                ("serial_number", models.CharField(max_length=1028)),
                ("release_date", models.DateField()),
                ("region", models.CharField(max_length=1028)),
                (
                    "developer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="developed_games",
                        to="games.gamecompany",
                    ),
                ),
                (
                    "game",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="games.game"
                    ),
                ),
                (
                    "platform",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="games",
                        to="games.gameplatform",
                    ),
                ),
                (
                    "publisher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="published_games",
                        to="games.gamecompany",
                    ),
                ),
            ],
        ),
    ]
